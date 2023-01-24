use ndarray::{Array2, Array1, Axis};
use ndarray_npy::{ReadNpyError, ReadNpyExt, WriteNpyError, WriteNpyExt};
use std::{fs::File, io::BufWriter, time::Instant};
use rand::Rng;
use emcee::{Guess, Prob};

struct Model {
    data: Vec<f64>,
    error: Vec<f64>,
}

impl Prob for Model {
    fn lnlike(&self, params: &Guess) -> f32 {
        let simulated_data = model(params[0]);
        let mut sum = 0.0;
        for (sim, (data, error)) in simulated_data.into_iter()
        .zip(self.data.iter().zip(self.error.iter())) {
            sum += ((*data as f32 - sim) / *error as f32).powi(2);
        }
        -0.5 * sum
    }

    fn lnprior(&self, params: &Guess) -> f32 {
        if 0.0 < params[0] || params[0] < 0.02 { 0.0 } else { -1e20 }
    }
}

fn model(param: f32) -> Vec<f32> {
    let mut simulated_data = Vec::with_capacity(1000);
    let mut x = 1.0;
    let mut v = 0.0;
    for _ in 0..1000 {
        v += -param * x;
        x += v;
        simulated_data.push(x);
    }
    simulated_data
}

fn run() {
    let mut rng = rand::thread_rng();
    let start_params = (0..32).map(|_| {Guess::new(&[rng.gen::<f32>() * 0.02])})
        .collect::<Vec<_>>();
    let model = read_data().unwrap();
    let mut sampler = emcee::EnsembleSampler::new(32, 1, &model).unwrap();
    sampler.run_mcmc(&start_params, 10_000).unwrap();
    let flat_samples = sampler.flatchain();
    save_data(flat_samples.into_iter().map(|g| {g[0]}).collect::<Vec<_>>()).unwrap();
}

fn main() {
    let now = Instant::now();
    run();
    let elapsed = now.elapsed();
    println!("Elapsed: {:?}", elapsed);
}

fn read_data() -> Result<Model, ReadNpyError> {
    let reader = File::open("../data.npy")?;
    let arr = Array2::<f64>::read_npy(reader)?;
    let mut iter = arr.axis_iter(Axis(0));
    Ok(Model {
        data: iter.next().unwrap().to_vec(),
        error: iter.next().unwrap().to_vec()
    })
}

fn save_data(vec: Vec<f32>) -> Result<(), WriteNpyError> {
    let writer = BufWriter::new(File::create("../mcmc-rust.npy")?);
    Array1::from_vec(vec).write_npy(writer)?;
    Ok(())
}


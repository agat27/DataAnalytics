data {
   int<lower=1> N; // number of data
   int<lower=1> M; // number of covariates
   matrix[M, N] X;
   array[N] real y;
}

parameters {
   vector[M] beta;
   real alpha;
   real<lower=0> sigma;
}

model {
   // Strongly regularzing priors on the slops
   beta ~ normal(0, 1);
   alpha ~ normal(0, 2);
   sigma ~ normal(0, 2);

   y ~ normal(X' * beta + alpha, sigma);
}
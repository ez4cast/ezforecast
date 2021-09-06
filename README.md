## eZforecast

A python library for time-series forecasting with easy manipulation of modern algorithms and techniques, this work focus on production-ready quality.

#### Data Loader
- [ ] `read_csv`: Loading time-series from csv file.
- [ ] `read_json`: Loading time-series from json file with pre-define schema.
- [ ] `read_rdbms`: Loading time-series from relational database management sytem with pre-define connection and schema.
- [ ] `read_bigquery`: Loading time-series from Google Cloud BigQuery.
- [ ] `read_readshift`: Loading time-series from Amazon RedShift.
- [ ] `read_snowflake`: Loading time-series from Snowflake.

#### Data Processor
- **Transformation**:
  - [ ] `Fourier`: Fourier transformation.
  - [ ] `Wavelet`: Wavelet transformation.
  - [ ] `EMD`: EMD transformation.
  - [ ] `EEMD`: EEMD transformation.
  - [ ] `PAA`: PAA transformation.
  - [ ] `SAX`: SAX transformation.
- **Sampler**:
  - [ ] ...

#### Model
- [ ] `Arima`: Auto-Regressive Integrated Moving Average.
- [ ] `LSTM`: Long Short Term Memory.
- [ ] `NBeats`: Neural basis expansion analysis for interpretable time series forecasting.
- [ ] `ConditionalNormalizingFlowLSTM`: Conditional Normalizing Flows LSTM.
- [ ] `TimescaleLSTM`: Timescale LSTM.
- [ ] `ODELSTM`: Ordinary differential equations with LSTM.
- [ ] `ESRNN`: Exponential smoothing - RNN. 
- [ ] `ES`: Simple exponential smoothing.
- [ ] `MTGNN`: Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks.
- [ ] `GNNLSTM`: GNN - LSTM.
- [ ] `Z-GCNET`: Time Zigzags at Graph Convolutional Networks for Time Series Forecasting
- [ ] `LiquidTimeconstantNetwork`: Liquid Time-constant Networks.
- [ ] `GRUODEBayes`: GRU-ODE-Bayes.

#### Loss
- [ ] ...

#### Metric
- [ ] ...

#### Trainer
- [ ] ...

#### Optimizer
- [ ] ....

#### Deployment
- [ ] `Loader`: Load saved pipeline.
- [ ] `Predictor`: Predictor instance for a pipeline.
- [ ] `Server`: REST API server.
- [ ] `Evaluator`: API benchmarking helpers.

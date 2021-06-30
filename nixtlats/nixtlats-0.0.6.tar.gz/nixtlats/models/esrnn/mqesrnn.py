# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/models_esrnn__mqesrnn.ipynb (unless otherwise specified).

__all__ = ['MQESRNN']

# Cell
from .esrnn import ESRNN

# Cell
class MQESRNN(ESRNN):
    def __init__(self,
                 n_series,
                 n_x,
                 n_s,
                 sample_freq,
                 input_size,
                 output_size,
                 es_component,
                 cell_type,
                 state_hsize,
                 dilations,
                 add_nl_layer,
                 learning_rate,
                 lr_scheduler_step_size,
                 lr_decay,
                 gradient_eps,
                 gradient_clipping_threshold,
                 rnn_weight_decay,
                 noise_std,
                 testing_percentiles,
                 training_percentiles,
                 loss,
                 val_loss):

        allowed_losses = ['MQ', 'wMQ']
        if loss not in allowed_losses:
            raise Exception(f'Loss {loss} not allowed')

        if val_loss is not None and val_loss not in allowed_losses:
            raise Exception(f'Val loss {val_loss} not allowed')

        allowed_es_component = ['median_residual', 'identity']

        if es_component not in allowed_es_component:
            raise Exception(f'es component {es_component} not allowed')

        level_variability_penalty = 0
        seasonality = []
        per_series_lr_multip = 1
        super(MQESRNN, self).__init__(n_series=n_series,
                                      n_s=n_s,
                                      n_x=n_x,
                                      sample_freq=sample_freq,
                                      input_size=input_size,
                                      output_size=output_size,
                                      es_component=es_component,
                                      cell_type=cell_type,
                                      state_hsize=state_hsize,
                                      dilations=dilations,
                                      add_nl_layer=add_nl_layer,
                                      seasonality=seasonality,
                                      learning_rate=learning_rate,
                                      lr_scheduler_step_size=lr_scheduler_step_size,
                                      lr_decay=lr_decay,
                                      per_series_lr_multip=per_series_lr_multip,
                                      gradient_eps=gradient_eps,
                                      gradient_clipping_threshold=gradient_clipping_threshold,
                                      rnn_weight_decay=rnn_weight_decay,
                                      noise_std=noise_std,
                                      level_variability_penalty=level_variability_penalty,
                                      testing_percentile=testing_percentiles,
                                      training_percentile=training_percentiles,
                                      loss=loss,
                                      val_loss=val_loss)
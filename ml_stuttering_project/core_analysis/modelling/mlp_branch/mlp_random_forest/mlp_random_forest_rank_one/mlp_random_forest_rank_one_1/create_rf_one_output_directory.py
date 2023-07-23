#!/usr/bin/env python
# coding: utf-8
from pathlib import Path
import os


class CreateRfOneDirectory:
    def __init__(self, results_dir, *args, **kwargs):
        super(CreateRfOneDirectory, self).__init__(*args, **kwargs)
        self.results_dir = results_dir
        self.rf_tf = self.propagate_dir(results_dir, 'rf_tf')
        self.rf_tf_rank_one_one_layer = self.propagate_dir(self.rf_tf, 'rf_tf_rank_one_one_layer')
        self.rf_tf_rank_one_one_layer_results = self.propagate_dir(self.rf_tf_rank_one_one_layer, 'rf_tf_rank_one_one_layer_results')
        self.rf_tf_rank_one_one_layer_epoch_select_model = self.propagate_dir(self.rf_tf_rank_one_one_layer,
                                                                       'rf_tf_rank_one_one_layer_epoch_select_model')
        self.rf_tf_rank_one_one_layer_final_model = self.propagate_dir(self.rf_tf_rank_one_one_layer, 'rf_tf_rank_one_one_layer_final_model')
        self.rf_tf_rank_one_one_layer_pretraining = self.propagate_dir(self.rf_tf_rank_one_one_layer, 'rf_tf_rank_one_one_layer_pretraining')
        self.rf_tf_rank_one_one_layer_tensorboard = self.propagate_dir(self.rf_tf_rank_one_one_layer_pretraining,
                                                                'rf_tf_rank_one_one_layer_tensorboard')
        self.rf_tf_rank_one_one_layer_partial_models = self.propagate_dir(self.rf_tf_rank_one_one_layer_pretraining,
                                                                   'rf_tf_rank_one_one_layer_partial_models')

    def propagate_dir(self, old_dir, sub_dir):
        new_dir = Path.home().joinpath(old_dir, str(sub_dir))
        if new_dir.exists():
            pass
        else:
            os.makedirs(new_dir)
        new_dir = str(new_dir)
        return new_dir

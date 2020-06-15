from torchvision import transforms

train_params_base = {
"LR": 2 ,
"MOMENTUM": 0.9 ,
"WEIGHT_DECAY": 1e-5,
"STEP_MILESTONES": [49,63],
"GAMMA": 0.2,
"NUM_EPOCHS": 70,
"BATCH_SIZE":128,
"train_transform": transforms.Compose([
                                      transforms.RandomCrop(32, padding = 4),
                                      transforms.RandomHorizontalFlip(),
                                      transforms.ToTensor(),
                                      transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
                                      ]),
"test_transform": transforms.Compose([
                                     transforms.ToTensor(),
                                     transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
                                     ]),
}

approach_params_finetuning = {
"classification_loss": "bce",
"distillation_loss": None,
"use_distillation" : False,
"use_variation" : False,
"use_exemplars": False,
"n_exemplars": 0
}

approach_params_lwf = {
"classification_loss": "bce",
"distillation_loss": "icarl",
"use_distillation" : False,
"use_variation" : False,
"use_exemplars": False,
"n_exemplars": 0
}

approach_params_icarl = {
"classification_loss": "bce",
"distillation_loss": "icarl",
"use_distillation" : True,
"use_variation" : False,
"use_exemplars": True,
"n_exemplars": 2000
}

approach_params_variation = {
"classification_loss": "bce",
"distillation_loss": "icarl",
"use_distillation" : True,
"use_variation" : True,
"use_exemplars": True,
"n_exemplars": 2000
}

def get_params(method):
    if method == "FINETUNING":
        return train_params_base, approach_params_finetuning
    elif method == "LWF":
        return train_params_base, approach_params_lwf
    elif method == "ICARL":
        return train_params_base, approach_params_icarl
    else:
        return train_params_base, approach_params_variation

#!/usr/bin/env python
"""WB-8618: warn the user if they are using a local key to log in to cloud"""
<<<<<<< HEAD

import random
import string
=======
>>>>>>> 272ce0aed8610df9e012b4645d00bac96d90d188

import pytest
import wandb
import wandb.errors


# function to generate a random alphanumeric key of 40 chars
def random_key():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(40))


if __name__ == "__main__":
    # api_key starts with "local", but base_url points to cloud
    with pytest.raises(wandb.errors.UsageError) as e:
<<<<<<< HEAD
        wandb.login(key=f"local-{random_key()}")
=======
        wandb.login(key="local-87eLxjoRhY6u2ofg63NAJo7rVYHZo4NGACOvpSsF}")
>>>>>>> 272ce0aed8610df9e012b4645d00bac96d90d188
        assert (
            "Attempting to use a local API key to connect to https://api.wandb.ai" in str(e.value)
        )

    # check that this logic does not apply if base_url is not cloud
<<<<<<< HEAD
    assert wandb.login(key=f"local-{random_key()}", host="https://api.wandb.test")
=======
    assert wandb.login(key="local-87eLxjoRhY6u2ofg63NAJo7rVYHZo4NGACOvpSsF", host="https://api.wandb.test")
>>>>>>> 272ce0aed8610df9e012b4645d00bac96d90d188

import numpy as np


def ising_board(shape):

  # Spin configuration
  spins = np.random.choice([-1, 1], size=shape)

  # Magnetic moment
  moment = 1

  # External magnetic field
  field = np.full(shape, 0)

  # Temperature (in units of energy)
  temperature = .1

  # Interaction (ferromagnetic if positive, antiferromagnetic if negative)
  interaction = 1

  t = 0
  while t<1000:
    spins = update(spins, temperature, interaction, moment, field)
    t += 1

  return spins

def get_probability(energy1, energy2, temperature):
  return np.exp((energy1 - energy2) / temperature)

def get_energy(spins, interaction,  moment, field):
  return -np.sum(
    interaction * spins * np.roll(spins, 1, axis=0) +
    interaction * spins * np.roll(spins, -1, axis=0) +
    interaction * spins * np.roll(spins, 1, axis=1) +
    interaction * spins * np.roll(spins, -1, axis=1)
  )/2 - moment * np.sum(field * spins)

def update(spins, temperature, interaction, moment, field):
  spins_new = np.copy(spins)
  i = np.random.randint(spins.shape[0])
  j = np.random.randint(spins.shape[1])
  spins_new[i, j] *= -1

  current_energy = get_energy(spins, interaction, moment, field)
  new_energy = get_energy(spins_new, interaction, moment, field)
  if get_probability(current_energy, new_energy, temperature) > np.random.random():
    return spins_new
  else:
    return spins

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

len(assistiram)

set(assistiram)

##print(set([1,2,3,1]))

print({4, 1,2,3,1})

type({1,2})

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}


for usuario in set(assistiram):
  print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning)

print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)

print(23 in fez_ds_mas_nao_fez_ml)

print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1,5,76,34,52,13,17}
len(usuarios)

usuarios.add(13)
len(usuarios)

usuarios.add(765)
len(usuarios)

print(usuarios)

usuarios = frozenset(usuarios)
print(usuarios)

type(usuarios)

## usuarios.add(134)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.split()

print(set(meu_texto.split()))
#entrada
import math

input = 0

#saida desejada
output = 0

#taxa de aprendizado
learning_rate = 0.1
#peso
input_weight = 0.5

error = math.inf
interation = 0

#neuronio virtual
bias = 1
bias_weight = 0.5



while not error ==0:
    interation +=1
    print('interação ',interation,'\n','peso',input_weight)
    #entrada
    print("Entrada", input , "Desejado", output)
    sum = (input * input_weight) + (bias * bias_weight)


    #função de ativação
    def activation(sum):
        if sum >= 0:
            return 1
        else:
            return 0


    # recebe a função de ativação
    outputAt = activation(sum)

    print("Saída ",output)

    #calcular o erro
    error = output - outputAt

    print("erro",error)

    if not error == 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)
print("Parabens aprendeu !")
"""Projetao controller."""
# Ricardo Henrique Avelar Matheus 15.118.334-0
# Projeto de Robótica - CCR240

"""OBS: A simulação pode variar devido a utilização da
física para porta de correr"""

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

def delay(time_milisec):
    timeValue = time_milisec/1000.0
    initTime = robot.getTime()
    timeLeft = 0.00
    while (timeLeft < timeValue):
        currentTime = robot.getTime()
        timeLeft = currentTime - initTime
        robot.step(timestep)


# Habilita os dispositivos dos motores
motorDireitoFrente = robot.getDevice('wheel1')
motorEsquerdoFrente = robot.getDevice('wheel2')
motorDireitoAtras = robot.getDevice('wheel3')
motorEsquerdoAtras = robot.getDevice('wheel4')

# Libera o giro dos motores
motorEsquerdoFrente.setPosition (float('+inf'))
motorDireitoFrente.setPosition (float('+inf'))
motorEsquerdoAtras.setPosition (float('+inf'))
motorDireitoAtras.setPosition (float('+inf'))

# Habilita os dispositivos dos motores do manipulador
manip1 = robot.getDevice('arm1')
manip2 = robot.getDevice('arm2')
manip3 = robot.getDevice('arm3')
manip4 = robot.getDevice('arm4')
manip5 = robot.getDevice('arm5')
finger1 = robot.getDevice('finger1')
finger2 = robot.getDevice('finger2')

# Definindo as operações
def atender_porta():
    # Andar para frente
    motorEsquerdoFrente.setVelocity(6.28)
    motorDireitoFrente.setVelocity(6.28)
    motorEsquerdoAtras.setVelocity(6.28)
    motorDireitoAtras.setVelocity(6.28)
    delay (27850)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Girar para direita
    motorEsquerdoFrente.setVelocity(5.00)
    motorDireitoFrente.setVelocity(-5.00)
    motorEsquerdoAtras.setVelocity(5.00)
    motorDireitoAtras.setVelocity(-5.00)
    delay (11000)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Andar para frente
    motorEsquerdoFrente.setVelocity(6.28)
    motorDireitoFrente.setVelocity(6.28)
    motorEsquerdoAtras.setVelocity(6.28)
    motorDireitoAtras.setVelocity(6.28)
    delay (11925)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)

def abrir_porta():
    # Girar para direita
    motorEsquerdoFrente.setVelocity(6.00)
    motorDireitoFrente.setVelocity(-6.00)
    motorEsquerdoAtras.setVelocity(6.00)
    motorDireitoAtras.setVelocity(-6.00)
    delay (11000)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Andar para trás
    motorEsquerdoFrente.setVelocity(-4)
    motorDireitoFrente.setVelocity(-4)
    motorEsquerdoAtras.setVelocity(-4)
    motorDireitoAtras.setVelocity(-4)
    delay (1500)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Mover o manipulador para abrir a porta    
    manip1.setPosition (1.475)
    manip2.setPosition (0.785)
    manip3.setPosition (-1.32)
    delay (1000)
    manip2.setPosition (0)
    manip4.setPosition (0)
    manip5.setPosition (-1.46)
    delay (1000)
    
    # Andar para frente
    motorEsquerdoFrente.setVelocity(6.28)
    motorDireitoFrente.setVelocity(6.28)
    motorEsquerdoAtras.setVelocity(6.28)
    motorDireitoAtras.setVelocity(6.28)
    delay (4000)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    manip1.setPosition (0)
    manip2.setPosition (0)
    manip3.setPosition (0)
    delay (1000)
    
    # Girar para esquerda
    motorEsquerdoFrente.setVelocity(-5.00)
    motorDireitoFrente.setVelocity(5.00)
    motorEsquerdoAtras.setVelocity(-5.00)
    motorDireitoAtras.setVelocity(5.00)
    delay (7000)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)

def pegar_entrega():
    # Andar para frente
    motorEsquerdoFrente.setVelocity(6.28)
    motorDireitoFrente.setVelocity(6.28)
    motorEsquerdoAtras.setVelocity(6.28)
    motorDireitoAtras.setVelocity(6.28)
    delay (2000)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    manip1.setPosition (0)
    manip2.setPosition (0)
    manip3.setPosition (0)
    delay (1000)
    
    # Manipular a encomenda
    manip1.setPosition (0)
    manip2.setPosition (-0.25)
    manip3.setPosition (-1.15)
    manip4.setPosition (-1.15)
    manip5.setPosition (0)
    finger1.setPosition (0.025)
    finger2.setPosition (0.025)
    delay (1000)
    
    finger1.setPosition (0)
    finger2.setPosition (0)
    delay (500)
    
    manip1.setPosition (0)
    manip2.setPosition (1.50)
    manip3.setPosition (-2.55)
    manip5.setPosition (0)
    delay (1000)
    
def voltar_base():
    # Andar para trás
    motorEsquerdoFrente.setVelocity(-6.28)
    motorDireitoFrente.setVelocity(-6.28)
    motorEsquerdoAtras.setVelocity(-6.28)
    motorDireitoAtras.setVelocity(-6.28)
    delay (11825)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Girar para esquerda
    motorEsquerdoFrente.setVelocity(-5.00)
    motorDireitoFrente.setVelocity(5.00)
    motorEsquerdoAtras.setVelocity(-5.00)
    motorDireitoAtras.setVelocity(5.00)
    delay (13700)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Andar para trás
    motorEsquerdoFrente.setVelocity(-6.28)
    motorDireitoFrente.setVelocity(-6.28)
    motorEsquerdoAtras.setVelocity(-6.28)
    motorDireitoAtras.setVelocity(-6.28)
    delay (25050)
    motorEsquerdoFrente.setVelocity(0)
    motorDireitoFrente.setVelocity(0)
    motorEsquerdoAtras.setVelocity(0)
    motorDireitoAtras.setVelocity(0)
    delay (1000)
    
    # Entregar a encomenda na mesa
    manip2.setPosition (0.5)
    manip3.setPosition (-1.5)
    delay (1000)
    manip1.setPosition (2)
    delay (1000)
    manip2.setPosition (-1.13)
    manip3.setPosition (-0.45)
    manip4.setPosition (-0.75)
    manip5.setPosition (0)
    delay (1000)
    finger1.setPosition (0.025)
    finger2.setPosition (0.025)
    delay (1000)
    manip1.setPosition (0)
    manip2.setPosition (1.50)
    manip3.setPosition (-2.55)
    manip5.setPosition (0)
    delay (1000)
    
# Main code
print("Atendendo a porta")
atender_porta()
print("Abrindo porta")
abrir_porta()
print("Recebendo entrega")
pegar_entrega()
print("Entrega recebida, voltando a base")
voltar_base()


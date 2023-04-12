## Librerias utilizadas
import cv2
import numpy as np
import os
import time

def filtroPol():
    ##Aqui se espesifica la ruta del video a nalizar
    cap = cv2.VideoCapture('./Data/pruebaHongo.mp4')

    ##Simple aqui solo se vefifica que el video es abto para reproduccirse
    if not cap.isOpened():
        print("No se pudo abrir el video compruebe que la dirección este bien")
        exit()

    ##Se decla una variable la cual ase referencia a mi contador de capturas
    contPho = 0;

    ##Aqui la capeta en donde se gurdan las capturas
    timActu = time.time()
    estruc = time.localtime(timActu)
    fechActual = time.strftime("%Y-%m-%d",estruc)
    ruCar = os.path.join(os.getcwd(), fechActual)
    #En caso de exitir se creara una con la fecha del dia que se ejecute
    pcar = './2023-04-10'
    if not os.path.exists(ruCar):
        os.makedirs(ruCar)

    ##Primera mascara de color
    hongoBajo1 = np.array([89, 100, 20], np.uint8)
    ##---------------------^---^^^---^------
    ##Con estos parametros los que se hace es rableser los valores de los colores
    ##Con el fin de sacar estos de una forma mas precisi lo que se realizo fue crear un rango mayor y menor
    hongoBajo2 = np.array([111, 100, 20], np.uint8)
    ##Segunda mascara de color
    hongoAlto1 = np.array([110, 255, 200], np.uint8)
    hongoAlto2 = np.array([138, 255, 200], np.uint8)

    while True:

        ret, frame = cap.read()
        if ret == True:
            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            maskRed1 = cv2.inRange(frameHSV, hongoBajo1, hongoAlto1)
            maskRed2 = cv2.inRange(frameHSV, hongoBajo2, hongoAlto2)
            maskRed = cv2.add(maskRed1, maskRed2)
            maskRedvis = cv2.bitwise_and(frame, frame, mask=maskRed)
         ##   ,contornos, = cv2.findContours(maskRed, cv2.RETR_EXTERNAL,
           ##    cv2.CHAIN_APPROX_SIMPLE)
           ## cv2.drawcortours(frame, contornos, -1, (255,0,0), 3)
            cv2.imshow('frame', frame)
            cv2.imshow('maskHongG', maskRed)
            cv2.imshow('maskHongGvis', maskRedvis)

            contPho +=1
            timeReload = 5

            if contPho %(5 *timeReload) == 0:
                rutaCap = os.path.join(pcar, "frame{}.jpg".format(contPho))
                cv2.imwrite(rutaCap, frame)


            ##En caso de querer de salir de ver los videos debe de precionar "S" para deter el proceso
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
    cap.release()
    cv2.destroyAllWindows()

    listElemt = os.listdir(ruCar)
    camtElemt = len(listElemt)
    #print(camtElemt)
    if  camtElemt >= 30:
        return "huitla"
    else:
        print("que brr")

def temperatura():

    cap = cv2.VideoCapture('./Data')

    # Limites  y rango del color rojo Prueba 2
    LimiteinferiorRojo1 = np.array([0, 100, 20], np.uint8)
    LimiteSuperiorRojo1 = np.array([1, 255, 255], np.uint8)

    # Segunda rango de limte color rojo seguna codigo de colocre hsv
    LimiteinferiorRojo2 = np.array([175, 100, 20], np.uint8)
    LimiteSuperiorRojo2 = np.array([179, 255, 255], np.uint8)

    while True:  # se inicia la camara  permiendo leer la imagen a cada momento
        ret, frame = cap.read()

        if ret == True:
            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # submascaras del color rojo
            maskroja1 = cv2.inRange(
                frameHSV, LimiteinferiorRojo1, LimiteSuperiorRojo1)
            maskroja2 = cv2.inRange(
                frameHSV, LimiteinferiorRojo2, LimiteSuperiorRojo2)
            # mascara de color rojo con sus rangos
            maskroja = cv2.add(maskroja1, maskroja2)
            contornos, variable = cv2.findContours(
                maskroja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # mostras contornos en el video
            # primera prueba
            # cv2.drawContours(frame, contornos, -1, (0,255,0), 3)

            # seleccion de contornos
            for c in contornos:
                area = cv2.contourArea(c)
                if area > 3000:
                    # Buscar el area central del objeto especificado para  mostrarla
                    M = cv2.moments(c)
                    if (M["m00"] == 0):
                        M["m00"] = 1
                    # valores de x,y
                    x = int(M["m10"] / M["m00"])
                    y = int(M['m01'] / M['m00'])
                    # se dibuja el circulo
                    cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                    # fuente del texto
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    # colancandolo en la imagen
                    cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y),
                                font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
                    # suavizado de lineas
                    newContourn = cv2.convexHull(c)
                    # para dibujar solo ciertos contornos
                    cv2.drawContours(frame, [newContourn], 0, (0, 255, 0), 3)

            cv2.imshow('frame', frame)
            # cv2.imshow('maskRed', maskazul)
            # dIBUJAR LOS CONTRONOS ENCONTRADOS\

            if cv2.waitKey(40) & 0xFF == ord('s'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    filtroPol()
    #temperatura()

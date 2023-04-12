from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from datetime import datetime
from datetime import date
import conexion_mongo as dbase
import sys
import dbiot as con
import monitoreo
import os
import analisis as a
#import consultarclima


today = date.today()

db1 = con.dbConexion()

db = dbase.dbConexion()

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
monitoreo.create_dash(app)
#a=("n")
nombreUser = ()
a = (a.filtroPol())
error = ("")

# Creamos nuestro primer route. '/login'


@app.route('/')
def template():
    # Renderizamos la plantilla. Formulario HTML.
    # templates/form.html
    # usuario = db['usuario']

    return render_template("index.html")


# Definimos el route con el método GET

@app.route('/perfil', methods=['GET', 'POST'])
def usuario():
    global nombreUser, today
    collection = db['usuario']
    # Obtenemos la información del parametro "nombreUser"
    # Esto lo hacemos con "request.args.get"
    nombreUser = request.args.get('nombreUser')
    contraseña = request.args.get('contrasenia')
    usuario_encontrado = collection.find_one({"usuario": nombreUser})
    if usuario_encontrado and usuario_encontrado["contrasenia"] == contraseña:
        if a == "n":
            f = "El tipo de plaga que se encontro fue Gusano cogollero"
            l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
            g = "Clorpirifos: Es un insecticida organofosforado que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
            h = "Lambda-cihalotrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa atacando el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
            i = "Emamectina benzoato: Es un insecticida de la familia de las avermectinas que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o inyectado en el suelo."
            j = "Deltametrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."

        elif a == "huitla":
            f = "Se detecto un brote de huitlacoche en el área"
            l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos pesticidas"
            g = "Azoxistrobina: actúa inhibiendo la respiración mitocondrial de los hongos, lo que interfiere en su capacidad para generar energía, crecer y reproducirse. Es efectiva contra una amplia gama de hongos, incluyendo oomicetos, ascomicetos y basidiomicetos, y se utiliza para el control de enfermedades como mildiu, roya, manchas foliares y otras infecciones fungosas en diferentes cultivos."
            h = "Clorotalonil:  actúa como un inhibidor de la respiración mitocondrial de los hongos, lo que interfiere en su capacidad para generar energía, crecer y reproducirse. Es efectivo contra una amplia gama de hongos, incluyendo oomicetos, ascomicetos y basidiomicetos, y se utiliza para el control de enfermedades como mildiu, roya, manchas foliares y otras infecciones fungosas en diferentes cultivos."
            i = "Tebuconazol: es un fungicida sistémico preventivo y curativo, recomendado para el control de enfermedades en vides, viñas, frutales y pinos señalados en esta etiqueta, así como también puede ser utilizado en tratamiento de postcosecha en cerezas, duraznos, ciruelas y nectarines."
            j = "Fludioxonil: actúa como un inhibidor de la germinación de esporas de hongos, lo que impide su capacidad para colonizar las plantas y causar infecciones. Es efectivo contra una amplia gama de hongos, incluyendo ascomicetos y basidiomicetos, y se utiliza para el control de enfermedades como podredumbre de raíz, podredumbre de frutas y otros problemas fungosos en diferentes cultivos."

        elif a == "b":
            f = "El tipo de plaga que se encontro fue Gusano elotero"
            l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
            g = "Clorpirifos: Es un insecticida organofosforado que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
            h = "Lambda-cihalotrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa atacando el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
            i = "Emamectina benzoato: Es un insecticida de la familia de las avermectinas que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o inyectado en el suelo."
            j = "Deltametrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."

        elif a == "a":
            l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
            f = "El tipo de plaga que se encontro fue Gusano soldado"
            g = "Bacillus thuringiensis (Bt): Es un insecticida biológico derivado de una bacteria del suelo que es efectivo contra muchas especies de larvas de insectos, incluyendo las de gusanos soldados. Actúa como una toxina que afecta el sistema digestivo del insecto, provocando su muerte. Se aplica en forma de pulverización foliar."
            h = "Deltametrina: Es un insecticida piretroide que actúa sobre el sistema nervioso del insecto, provocando una parálisis y muerte. Se aplica en forma de pulverización foliar o en forma de gránulos en el suelo."
            i = "Clorpirifos: Es un insecticida organofosforado que actúa como un inhibidor de la colinesterasa en el sistema nervioso del insecto, causando parálisis y muerte. Se aplica en forma de pulverización foliar."
            j = "Carbaryl: Es un insecticida carbamato que actúa sobre el sistema nervioso del insecto, provocando una parálisis y muerte. Se aplica en forma de pulverización foliar."
        elif a == "c":
            l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
            f = "El tipo de plaga que se encontro fue Araña roja"
            g = "Acaricidas organofosforados: Ejemplos de acaricidas organofosforados utilizados para el control de la araña roja incluyen clorpirifos, diazinón, malatión y azinfos-metilo. Estos insecticidas actúan interfiriendo con el sistema nervioso del ácaro, causando parálisis y muerte."
            h = "Acaricidas piretroides: Ejemplos de acaricidas piretroides utilizados para el control de la araña roja incluyen bifentrina, cipermetrina, y permetrina. Estos insecticidas actúan sobre el sistema nervioso del ácaro, provocando parálisis y muerte."
            i = "Acaricidas organoclorados: Ejemplos de acaricidas organoclorados utilizados para el control de la araña roja incluyen dicofol y clordecona. Estos insecticidas actúan interfiriendo con el sistema nervioso del ácaro, causando parálisis y muerte."
            j = "Acaricidas carbamatos: Ejemplos de acaricidas carbamatos utilizados para el control de la araña roja incluyen propoxur y carbaril. Estos insecticidas actúan interfiriendo con el sistema nervioso del ácaro, provocando parálisis y muerte."
        else:
            f = "No se encontro ningun tipo de problema en el area"
            g = "No se requiere de ningun tipo de atencion"
            h =""
            i=""
            j=""
            l=""
        return render_template("perfil.html", today=today, f=f, g=g, h=h, i=i, j=j, l=l)
    else:
        n = "Usuario o contraseña incorrectos"
        return render_template("index.html", n=n)


@app.route('/informacion')
def info():
    if a == "n":
        f = "El gusano cogollero se alimenta de cultivos como maíz, algodón, granos"\
            " pequeños, soya, pimiento y tomate. El"\
            " daño ocurre cuando la larva perfora las"\
            " flores y frutas de la planta hospedera"\
            " y se alimenta dentro de la planta; las"\
            " larvas también pueden alimentarse de"\
            " las hojas de las plantas hospederas. Esta"\
            " plaga invasiva se puede encontrar tanto"\
            " en los ambientes del campo como en los"\
            " invernaderos."
    elif a == "b":
        f = "El gusano elotero es una larva de polilla que afecta a los cultivos de maíz. Su nombre científico es Helicoverpa zea y es conocido con varios nombres comunes en diferentes regiones,"\
            " como gusano del maíz, barrenador del maíz, oruga cogollera, entre otros."\
            "El gusano elotero es considerado una plaga agrícola debido a que se alimenta"\
            " de las mazorcas de maíz, causando daños en la producción y calidad del cultivo."\
            " Las larvas del gusano elotero se alimentan de los granos de maíz y pueden causar daños directos, como"\
            "la destrucción de los granos y la reducción del rendimiento del cultivo, así como daños indirectos al permitir"\
            " la entrada de hongos y bacterias que pueden provocar pudriciones y enfermedades en las mazorcas."
    elif a == "huitla":
        f = "El huitlacoche es un hongo comestible que infecta a las mazorcas"\
            " de maíz, y su control no suele requerir el uso de pesticidas químicos."\
            " El huitlacoche se considera una delicadeza culinaria en algunas culturas y"\
            " se utiliza en la cocina mexicana y de otros países para preparar platillos tradicionales."
    elif a == "a":
        f = "Los gusanos soldados (Hermetia illucens), también conocidos como larvas de mosca soldado"\
            " negra, generalmente no causan problemas en el maíz, ya que su dieta se compone principalmente"\
            " de materia orgánica en descomposición, como estiércol y residuos de alimentos. Sin embargo,"\
            " en casos excepcionales, las larvas de gusano soldado podrían ocasionalmente alimentarse"\
            " de plantas de maíz en condiciones de alta densidad poblacional o cuando no encuentran suficiente alimento disponible."
    elif a == "c":
        f = "Daños en las hojas: La araña roja se alimenta de las hojas de maíz, perforando las células de la epidermis y succionando los contenidos celulares. Esto puede causar decoloración de las hojas, amarillamiento, manchas"\
            " y necrosis, lo que afecta la capacidad de la planta para realizar la fotosíntesis y producir nutrientes."\
            "Reducción del rendimiento: Los daños en las hojas causados por la araña roja pueden reducir la capacidad de la planta de maíz para producir carbohidratos y desarrollar adecuadamente las mazorcas, lo que puede resultar en una disminución del rendimiento del cultivo."\
            "Transmisión de enfermedades: La araña roja también puede actuar como vector de enfermedades virales en el maíz, transmitiendo virus de una planta a otra durante su alimentación."\
            " Esto puede tener un impacto negativo en la salud y rendimiento del cultivo."

    else:
        f = "No se encontro ningun tipo de problema en el area"

    return render_template("informacion.html", f=f)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html", error=error)


@app.route('/datos', methods=['GET', 'POST'])
def datos():
    global error
    collection = db['usuario']
    Usuario = request.args.get('Usuario')
    contra = request.args.get('contra')
    ubi = request.args.get('ubicacion')
    usuario_encontrado = collection.find_one({"usuario": Usuario})

    if Usuario == "" or contra == "" or ubi == "":
        error = "Rellene todos los campos"
        return render_template("register.html", error=error)
    elif usuario_encontrado and usuario_encontrado["usuario"] == Usuario:
        error = "Nombre de usuario en uso"
        return render_template("register.html", error=error)
    else:
        data = {
            "usuario": Usuario,
            "contrasenia": contra,
            "ubicacion": ubi
        }
        collection.insert_one(data)
        return render_template("index.html")


@app.route('/perfil1')
def perfil():
    if a == "n":
        f = "El tipo de plaga que se encontro fue Gusano cogollero"
        l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
        g = "Clorpirifos: Es un insecticida organofosforado que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
        h = "Lambda-cihalotrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa atacando el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
        i = "Emamectina benzoato: Es un insecticida de la familia de las avermectinas que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o inyectado en el suelo."
        j = "Deltametrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."

    elif a == "b":
        f = "El tipo de plaga que se encontro fue Gusano elotero"
        l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
        g = "Clorpirifos: Es un insecticida organofosforado que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
        h = "Lambda-cihalotrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa atacando el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
        i = "Emamectina benzoato: Es un insecticida de la familia de las avermectinas que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o inyectado en el suelo."
        j = "Deltametrina: Es un insecticida piretroide que se utiliza para el control del gusano cogollero en diferentes cultivos. Actúa interfiriendo con el sistema nervioso del insecto y puede ser aplicado en forma de spray o granulado."
    elif a == "huitla":
        f = "Se detecto un brote de huitlacoche en el área"
        l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos pesticidas"
        g = "Azoxistrobina: actúa inhibiendo la respiración mitocondrial de los hongos, lo que interfiere en su capacidad para generar energía, crecer y reproducirse. Es efectiva contra una amplia gama de hongos, incluyendo oomicetos, ascomicetos y basidiomicetos, y se utiliza para el control de enfermedades como mildiu, roya, manchas foliares y otras infecciones fungosas en diferentes cultivos."
        h = "Clorotalonil:  actúa como un inhibidor de la respiración mitocondrial de los hongos, lo que interfiere en su capacidad para generar energía, crecer y reproducirse. Es efectivo contra una amplia gama de hongos, incluyendo oomicetos, ascomicetos y basidiomicetos, y se utiliza para el control de enfermedades como mildiu, roya, manchas foliares y otras infecciones fungosas en diferentes cultivos."
        i = "Tebuconazol: es un fungicida sistémico preventivo y curativo, recomendado para el control de enfermedades en vides, viñas, frutales y pinos señalados en esta etiqueta, así como también puede ser utilizado en tratamiento de postcosecha en cerezas, duraznos, ciruelas y nectarines."
        j = "Fludioxonil: actúa como un inhibidor de la germinación de esporas de hongos, lo que impide su capacidad para colonizar las plantas y causar infecciones. Es efectivo contra una amplia gama de hongos, incluyendo ascomicetos y basidiomicetos, y se utiliza para el control de enfermedades como podredumbre de raíz, podredumbre de frutas y otros problemas fungosos en diferentes cultivos."

    elif a == "a":
        l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
        f = "El tipo de plaga que se encontro fue Gusano soldado"
        g = "Bacillus thuringiensis (Bt): Es un insecticida biológico derivado de una bacteria del suelo que es efectivo contra muchas especies de larvas de insectos, incluyendo las de gusanos soldados. Actúa como una toxina que afecta el sistema digestivo del insecto, provocando su muerte. Se aplica en forma de pulverización foliar."
        h = "Deltametrina: Es un insecticida piretroide que actúa sobre el sistema nervioso del insecto, provocando una parálisis y muerte. Se aplica en forma de pulverización foliar o en forma de gránulos en el suelo."
        i = "Clorpirifos: Es un insecticida organofosforado que actúa como un inhibidor de la colinesterasa en el sistema nervioso del insecto, causando parálisis y muerte. Se aplica en forma de pulverización foliar."
        j = "Carbaryl: Es un insecticida carbamato que actúa sobre el sistema nervioso del insecto, provocando una parálisis y muerte. Se aplica en forma de pulverización foliar."
    elif a == "c":
        f = "El tipo de plaga que se encontro fue Araña roja"
        l = "Se recomienda llevar a cabo una fumigacion. A continuacion se recomiendan algunos insecticidas"
        g = "Acaricidas organofosforados: Ejemplos de acaricidas organofosforados utilizados para el control de la araña roja incluyen clorpirifos, diazinón, malatión y azinfos-metilo. Estos insecticidas actúan interfiriendo con el sistema nervioso del ácaro, causando parálisis y muerte."
        h = "Acaricidas piretroides: Ejemplos de acaricidas piretroides utilizados para el control de la araña roja incluyen bifentrina, cipermetrina, y permetrina. Estos insecticidas actúan sobre el sistema nervioso del ácaro, provocando parálisis y muerte."
        i = "Acaricidas organoclorados: Ejemplos de acaricidas organoclorados utilizados para el control de la araña roja incluyen dicofol y clordecona. Estos insecticidas actúan interfiriendo con el sistema nervioso del ácaro, causando parálisis y muerte."
        j = "Acaricidas carbamatos: Ejemplos de acaricidas carbamatos utilizados para el control de la araña roja incluyen propoxur y carbaril. Estos insecticidas actúan interfiriendo con el sistema nervioso del ácaro, provocando parálisis y muerte."
    else:
        f = "No se encontro ningun tipo de problema en el area"
        g = "No se requiere de ningun tipo de atencion"
    return render_template("perfil.html", today=today, f=f, g=g, h=h, i=i, j=j, l=l)


@app.route("/m")
def dash_temp():
    return redirect("/dashb")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=port)

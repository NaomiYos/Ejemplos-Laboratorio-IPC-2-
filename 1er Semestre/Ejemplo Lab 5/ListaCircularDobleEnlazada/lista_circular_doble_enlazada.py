from cgi import print_form
from tempfile import tempdir
from curso import Curso

class ListaCircularDobleEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False

    def agregarPrimero(self, codigo, nombre, creditos):
        nuevo=Curso(codigo,nombre,creditos)   

        if self.estaVacia():
            self.primero=self.ultimo=nuevo 
        else:
            tmp=nuevo
            tmp.siguiente=self.primero
            self.primero.anterior=tmp
            self.primero=tmp
        self.__unir_nodos()

    def agregarUltimo(self, codigo, nombre, creditos):
        nuevo=Curso(codigo,nombre,creditos)   

        if self.estaVacia():
            self.primero=self.ultimo=nuevo 
        else:
            tmp=self.ultimo
            self.ultimo=tmp.siguiente=nuevo
            self.ultimo.anterior=tmp
        self.__unir_nodos()

    def __unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero

    def eliminar_inicio(self):
        if self.estaVacia():
            print("La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            self.primero=self.primero.siguiente
        self.__unir_nodos()    

    def eliminar_ultimo(self):
        if self.estaVacia():
            print("La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            self.ultimo=self.ultimo.anterior    
        self.__unir_nodos()    

    def recorrer_inicio_fin(self):
        tmp=self.primero
        while tmp:
            print(tmp.codigo,tmp.nombre,tmp.creditos)
            tmp=tmp.siguiente
            if tmp==self.primero:
                break

    def recorrer_fin_inicio(self):
        tmp=self.ultimo
        while tmp:
            print(tmp.codigo,tmp.nombre,tmp.creditos)
            tmp=tmp.anterior
            if tmp==self.ultimo:
                break

    def buscar(self,codigo,nombre,creditos):
        busqueda=Curso(codigo, nombre, creditos)

        aux=self.primero
        while aux:
            if aux.nombre==busqueda.nombre:
                return True
            else:
                aux=aux.siguiente
                if aux==self.primero:
                    return False    



    def report(self):
        aux=self.primero
        text=""
        text+="rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n"
        text+="labelloc = \"t;\"label = \"Cursos\";\n"

        while aux:
            text+="x"+str(aux.codigo)+"[dir=both label = \"Codigo = "+str(aux.codigo)+"\\nNombre = "+aux.nombre+"\\n Creditos = "+str(aux.creditos)+ "\"]"
            text+="x"+str(aux.codigo)+"-> x"+str(aux.siguiente.codigo)+"\n"
            text+="x"+str(aux.codigo)+"-> x"+str(aux.anterior.codigo)+"\n"
            aux=aux.siguiente
            if aux!=self.primero:    
                text+="x"+str(aux.codigo)+"[dir=both label = \"Codigo = "+str(aux.codigo)+"\\nNombre = "+aux.nombre+"\\n Creditos = "+str(aux.creditos)+ "\"]"
                print(text)
            if aux==self.ultimo:
                text+="x"+str(aux.codigo)+"-> x"+str(aux.siguiente.codigo)+"\n"
                text+="x"+str(aux.codigo)+"-> x"+str(aux.anterior.codigo)+"\n"
                break
        return text

    def crearReporte(self):
        contenido="digraph G {\n\n"
        r = open("reporte.txt","w")
        contenido+=str(self.report())
        contenido+='\n}'
        r.write(contenido)
        r.close()
        print("done")
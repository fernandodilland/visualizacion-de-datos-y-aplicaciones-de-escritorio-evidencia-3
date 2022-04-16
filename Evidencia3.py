import sys, csv
import pandas as pd
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

class Alumnos_GUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Proyectos\Python\UI\Alumnos.ui", self)
        self.fn_init_UI()

    #Generacion de Funcion Init_UI
    def fn_init_UI(self):

        #Conectar funcion registrar al boton registrar
        self.btn_Registrar.clicked.connect(self.fn_registrar)

        #Conectar funcion consultar al boton consultar
        self.btn_Consultar.clicked.connect(self.fn_consultar)

        #Conectar funcion fn_leer_csv al boton Leer CSV
        self.btn_Leer.clicked.connect(self.fn_leer_csv)

        #Conectar funcion fn_leer_csv al boton Leer CSV
        self.btn_Grabar.clicked.connect(self.fn_grabar_csv)

        #Conectar funcion fn_limiar al boton Limpiar
        self.btn_Limpiar.clicked.connect(self.fn_limpiar)

        #Conectar funcion fn_eliminar al boton Eliminar
        self.btn_Eliminar.clicked.connect(self.fn_eliminar)


    #Generacion de Funcion Registrar
    def fn_registrar(self):
       #self.edt_matricula.setText('Funcion Registrar')   
        rowPosition = self.Tabla_Datos.rowCount()
        self.Tabla_Datos.insertRow(rowPosition)   
        
        #Campo Matricula
        newItem = QTableWidgetItem(self.edt_matricula.text())
        self.Tabla_Datos.setItem(rowPosition, 0, newItem); 

        #Campo Nombre
        newItem = QTableWidgetItem(self.edt_nombre.text())
        self.Tabla_Datos.setItem(rowPosition, 1, newItem); 

        #Campo App Paterno
        newItem = QTableWidgetItem(self.edt_apppat.text())
        self.Tabla_Datos.setItem(rowPosition, 2, newItem); 

        #Campo App Materno
        newItem = QTableWidgetItem(self.edt_appmat.text())
        self.Tabla_Datos.setItem(rowPosition, 3, newItem); 

        #Campo Domicilio
        newItem = QTableWidgetItem(self.edt_domicilio.text())
        self.Tabla_Datos.setItem(rowPosition, 4, newItem); 

        #Campo Ciudad, pendiente tomar valor del combobox
        newItem = QTableWidgetItem(self.cbx_ciudad.currentText())
        self.Tabla_Datos.setItem(rowPosition, 5, newItem); 

        #Campo Estado, pendiente tomar valor del combobox
        newItem = QTableWidgetItem(self.cbx_estado.currentText())
        self.Tabla_Datos.setItem(rowPosition, 6, newItem); 

        #Campo Carrera pendiente tomar valor del combobox
        newItem = QTableWidgetItem(self.cbx_carrera.currentText())
        self.Tabla_Datos.setItem(rowPosition, 7, newItem); 

        #Campo Sexo
        newItem = QTableWidgetItem(self.check_sexo())
        self.Tabla_Datos.setItem(rowPosition, 8, newItem); 

        #Campo Edad
        newItem = QTableWidgetItem(str(self.spinEdad.value()))
        self.Tabla_Datos.setItem(rowPosition, 9, newItem); 

        #Campo Beca
        newItem = QTableWidgetItem(self.check_beca())
        self.Tabla_Datos.setItem(rowPosition, 10, newItem); 

        #Campo Foraneo
        newItem = QTableWidgetItem(self.check_generico(self.chk_foraneo))
        self.Tabla_Datos.setItem(rowPosition, 11, newItem); 

        #Campo Habla Ingles
        newItem = QTableWidgetItem(self.check_generico(self.chk_ingles))
        self.Tabla_Datos.setItem(rowPosition, 12, newItem); 

        #Campo Materia Favorita Programacion
        newItem = QTableWidgetItem(self.check_generico(self.chk_prog))
        self.Tabla_Datos.setItem(rowPosition, 13, newItem); 

        #Campo Materia Favorita Base de Datos
        newItem = QTableWidgetItem(self.check_generico(self.chk_bd))
        self.Tabla_Datos.setItem(rowPosition, 14, newItem); 

        #Campo Materia Favorita Contabilidad
        newItem = QTableWidgetItem(self.check_generico(self.chk_contab))
        self.Tabla_Datos.setItem(rowPosition, 15, newItem); 

        #Campo Materia Favorita Estadística
        newItem = QTableWidgetItem(self.check_generico(self.chk_estadistica))
        self.Tabla_Datos.setItem(rowPosition, 16, newItem); 

        #Campo Materia Favorita Investigacion de Operaciones
        newItem = QTableWidgetItem(self.check_generico(self.chk_inv_op))
        self.Tabla_Datos.setItem(rowPosition, 17, newItem); 


        #Agregar estas 2 lineas por cada columna a agregar
        #newItem = QTableWidgetItem(tomar el valor de component o funcion)
        #self.Tabla_Datos.setItem(rowPosition, incrementar columna, newItem); 


   # method called by radio button
    def check_sexo(self):
            
        # checking if it is checked
        if self.radio_hombre.isChecked():
              
            # changing text of label
            vsexo = self.radio_hombre.text()
  
        # if it is not checked
        else:
              
            # changing text of label
            vsexo = self.radio_mujer.text()

        return vsexo


   # Validar Porcentaje de Beca
    def check_beca(self):
          
        # Valor de beca = 0
        if self.radio_cero.isChecked():
              
            #beca cero
            vbeca = self.radio_cero.text()

        # if it is not checked
        else:
              
            if self.radio_50.isChecked():
                # beca 50
                vbeca = self.radio_50.text()

            else:    
                if self.radio_80.isChecked():
                    # beca 80
                    vbeca = self.radio_80.text()
                else:    
                    vbeca = self.radio_100.text()
        return vbeca


    def check_generico(self,QCheckBox):
        if QCheckBox.isChecked():
            vcheck='1'
        else:
            vcheck='0'

        return vcheck
      
                
    #Generacion de Funcion Consultar
    def fn_consultar(self):
       self.edt_nombre.setText('Funcion Consultar')         

    #Generacion de Funcion Leer de CSV
    def fn_leer_csv(self):
        #self.edt_apppat.setText('Funcion Leer desde CSV')
        index=0
        with open(r'C:\Proyectos\Python\UI\alumnos2.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                #print(row)
                #print(row[0], row[1])

                if index>0:  
                    rowPosition = self.Tabla_Datos.rowCount()
                    self.Tabla_Datos.insertRow(rowPosition)   
        
                    #Campo Matricula
                    newItem = QTableWidgetItem(row[0])
                    self.Tabla_Datos.setItem(rowPosition, 0, newItem); 

                    #Campo Nombre
                    newItem = QTableWidgetItem(row[1])
                    self.Tabla_Datos.setItem(rowPosition, 1, newItem); 

                    #Campo App Paterno
                    newItem = QTableWidgetItem(row[2])
                    self.Tabla_Datos.setItem(rowPosition, 2, newItem); 

                    #Campo App Materno
                    newItem = QTableWidgetItem(row[3])
                    self.Tabla_Datos.setItem(rowPosition, 3, newItem); 

                    #Campo Domicilio
                    newItem = QTableWidgetItem(row[4])
                    self.Tabla_Datos.setItem(rowPosition, 4, newItem); 

                    #Campo Ciudad, pendiente tomar valor del combobox
                    newItem = QTableWidgetItem(row[5])
                    self.Tabla_Datos.setItem(rowPosition, 5, newItem); 

                    #Campo Estado, pendiente tomar valor del combobox
                    newItem = QTableWidgetItem(row[6])
                    self.Tabla_Datos.setItem(rowPosition, 6, newItem); 

                    #Campo Carrera pendiente tomar valor del combobox
                    newItem = QTableWidgetItem(row[7])
                    self.Tabla_Datos.setItem(rowPosition, 7, newItem); 

                    #Campo Sexo
                    newItem = QTableWidgetItem(row[8])
                    self.Tabla_Datos.setItem(rowPosition, 8, newItem); 

                    #Campo Edad
                    newItem = QTableWidgetItem(row[9])
                    self.Tabla_Datos.setItem(rowPosition, 9, newItem); 

                    #Campo Beca
                    newItem = QTableWidgetItem(row[10])
                    self.Tabla_Datos.setItem(rowPosition, 10, newItem); 

                    #Campo Foraneo
                    newItem = QTableWidgetItem(row[11])
                    self.Tabla_Datos.setItem(rowPosition, 11, newItem); 

                    #Campo Habla Ingles
                    newItem = QTableWidgetItem(row[12])
                    self.Tabla_Datos.setItem(rowPosition, 12, newItem); 

                    #Campo Materia Favorita Programacion
                    newItem = QTableWidgetItem(row[13])
                    self.Tabla_Datos.setItem(rowPosition, 13, newItem); 

                    #Campo Materia Favorita Base de Datos
                    newItem = QTableWidgetItem(row[14])
                    self.Tabla_Datos.setItem(rowPosition, 14, newItem); 

                    #Campo Materia Favorita Contabilidad
                    newItem = QTableWidgetItem(row[15])
                    self.Tabla_Datos.setItem(rowPosition, 15, newItem); 

                    #Campo Materia Favorita Estadística
                    newItem = QTableWidgetItem(row[16])
                    self.Tabla_Datos.setItem(rowPosition, 16, newItem); 

                    #Campo Materia Favorita Investigacion de Operaciones
                    newItem = QTableWidgetItem(row[17])
                    self.Tabla_Datos.setItem(rowPosition, 17, newItem); 
                    
                index+=1



    #Generacion de Funcion Grabar CSV
    def fn_grabar_csv(self):
        #self.edt_appmat.setText('Funcion Grabar CSV')
        columnHeaders = []

        # Create Columns Header List
        for j in range(self.Tabla_Datos.columnCount()):
            columnHeaders.append(self.Tabla_Datos.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        #create datafram object recordset
        for row in range(self.Tabla_Datos.rowCount()):          
            for col in range(self.Tabla_Datos.columnCount()):
                var1 = self.Tabla_Datos.item(row,col).text()
                print(var1)
                df.at[row, columnHeaders[col]] = self.Tabla_Datos.item(row,col).text()
        
        df.to_csv('alumnos3.csv', index=False)
 
        #print(df)


        #myData = [["first_name", "second_name", "Grade"],
        #  ['Alex', 'Brian', 'A'],
        #  ['Tom', 'Smith', 'B']]
 
        #myFile = open('example2.csv', 'w')
        #with myFile:
        #    writer = csv.writer(myFile)
        #    writer.writerows(myData)


    #Generacion de Funcion Grabar CSV
    def fn_limpiar(self):
        self.edt_matricula.clear()
        self.edt_nombre.clear()
        self.edt_apppat.clear()
        self.edt_appmat.clear()
        self.edt_domicilio.clear()
        self.chk_prog.setChecked(False)
        self.chk_bd.setChecked(False)
        self.chk_contab.setChecked(False)                
        self.chk_estadistica.setChecked(False)
        self.chk_inv_op.setChecked(False)                
        self.chk_foraneo.setChecked(False)
        self.chk_ingles.setChecked(False)
        self.radio_hombre.setChecked(False)
        self.radio_mujer.setChecked(False)        
        self.radio_cero.setChecked(False)        
        self.radio_50.setChecked(False)        
        self.radio_80.setChecked(False)        
        self.radio_100.setChecked(False)       
        #self.cbx_carrera.itemText(0) 
        self.edt_matricula.setFocus()

    #Generacion de Funcion Eliminar
    def fn_eliminar(self):
        #self.spinEdad.setValue(21)

        fila_seleccionada = self.Tabla_Datos.selectedItems()

        if fila_seleccionada:

            fila = fila_seleccionada[0].row()
            self.Tabla_Datos.removeRow(fila)
            self.Tabla_Datos.clearSelection()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Alumnos_GUI()
    GUI.show()
    sys.exit(app.exec_())
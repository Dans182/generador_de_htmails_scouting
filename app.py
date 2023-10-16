import tkinter as tk
import tkinter.scrolledtext as tkst

def generar_mensaje():
    nombre_scout = nombre_scout_entry.get()
    nombre_jugador = nombre_player_entry.get()
    numero_identificacion = id_entry.get()
    lenguaje = "español" if idioma.get() == 1 else "inglés"
    tipo_scout = scout_var.get()
    tipo_contacto = primer_contacto_var.get()
    
    if lenguaje == "español":
        if tipo_scout == "Scout de Porteros":
            tipo_scout_text = "Scout de Porteros"
        elif tipo_scout == "Scout de Mediocampos":
            tipo_scout_text = "Scout de Mediocampos"
        else:
            tipo_scout_text = "Tipo de Scout no seleccionado"
        
        if tipo_contacto == "Primer contacto manager":
            pregunta = "¿Qué plan de entrenamiento tienes para este jugador?"
        elif tipo_contacto == "Proponer plan de entrenamiento":
            pregunta = "Idealmente, el plan que sugerimos para un jugador como el tuyo sería:\n\n[plan de entrenamiento]\n\n¿Puedes seguir estos planes? Si no puedes, ¿qué es lo más cerca que puedes estar del plan?"
        else:
            pregunta = "Pregunta no seleccionada"
        
        intro = f"Hola,\n\nMi nombre es {nombre_scout} y soy {tipo_scout_text} de la selección nacional de Venezuela.\n"
        agradecimiento = f"Primero, quiero agradecerte por entrenar {nombre_jugador} ({numero_identificacion}). Tu jugador tiene posibilidades de jugar con nuestra selección en un futuro y apreciamos tu esfuerzo por entrenarlo."
        razon_del_contacto = f"{pregunta}"
        despedida = f"Saludos,\n{nombre_scout}"
    else:
        if tipo_scout == "Scout de Porteros":
            tipo_scout_text = "Goalkeeper Scout"
        elif tipo_scout == "Scout de Mediocampos":
            tipo_scout_text = "Midfield Scout"
        else:
            tipo_scout_text = "Scout type not selected"
        
        if tipo_contacto == "Primer contacto manager":
            pregunta = "What training plan do you have for him?"
        elif tipo_contacto == "Proponer plan de entrenamiento":
            pregunta = "Ideally, the plan we would suggest for a player like you would be:\n\n[training schedule].\n\nCan you follow this plan? If not, what is the closest you can get to the plan?"
        else:
            pregunta = "Question not selected"
        
        intro = f"Hello,\n\nMy name is {nombre_scout} and I am a {tipo_scout_text} of the Venezuelan National Team.\n"
        agradecimiento = f"First, I want to thank you for coaching {nombre_jugador} ({numero_identificacion}). Your player has a chance to play for our national team in the future and we appreciate your effort in coaching him."
        razon_del_contacto = f"{pregunta}"
        despedida = f"Regards,\n{nombre_scout}"
    
    mensaje_completo = intro + "\n\n" + agradecimiento + "\n\n" + razon_del_contacto + "\n\n" + despedida
    resultado_text.delete(1.0, tk.END)  # Borra el contenido anterior
    resultado_text.insert(tk.END, mensaje_completo)

app = tk.Tk()
app.title("Generador de Mensajes")

nombre_scout_label = tk.Label(app, text="Nombre:")
nombre_scout_label.pack()
nombre_scout_entry = tk.Entry(app)
nombre_scout_entry.pack()

nombre_player_label = tk.Label(app, text="Jugador:")
nombre_player_label.pack()
nombre_player_entry = tk.Entry(app)
nombre_player_entry.pack()

id_label = tk.Label(app, text="Número de Identificación:")
id_label.pack()
id_entry = tk.Entry(app)
id_entry.pack()

idioma_label = tk.Label(app, text="Selecciona el idioma:")
idioma_label.pack()
idioma = tk.IntVar()
espanol_radio = tk.Radiobutton(app, text="Español", variable=idioma, value=1)
ingles_radio = tk.Radiobutton(app, text="Inglés", variable=idioma, value=2)
espanol_radio.pack()
ingles_radio.pack()

scout_label = tk.Label(app, text="Selecciona el tipo de scout:")
scout_label.pack()
scout_var = tk.StringVar()
scout_var.set("Scout de Porteros")
scout_radio1 = tk.Radiobutton(app, text="Scout de Porteros", variable=scout_var, value="Scout de Porteros")
scout_radio2 = tk.Radiobutton(app, text="Scout de Mediocampos", variable=scout_var, value="Scout de Mediocampos")
scout_radio1.pack()
scout_radio2.pack()

primer_contacto_label = tk.Label(app, text="Selecciona el tipo de contacto:")
primer_contacto_label.pack()
primer_contacto_var = tk.StringVar()
primer_contacto_var.set("Primer contacto manager")
primer_contacto_radio1 = tk.Radiobutton(app, text="Primer contacto manager", variable=primer_contacto_var, value="Primer contacto manager")
primer_contacto_radio2 = tk.Radiobutton(app, text="Proponer plan de entrenamiento", variable=primer_contacto_var, value="Proponer plan de entrenamiento")
primer_contacto_radio3 = tk.Radiobutton(app, text="Pregunta no seleccionada", variable=primer_contacto_var, value="Pregunta no seleccionada")
primer_contacto_radio1.pack()
primer_contacto_radio2.pack()
primer_contacto_radio3.pack()

generar_button = tk.Button(app, text="Generar Mensaje", command=generar_mensaje)
generar_button.pack()

resultado_text = tkst.ScrolledText(app, wrap=tk.WORD, width=40, height=10)
resultado_text.pack()

app.mainloop()

import streamlit as st

st.set_page_config(
    page_title="Mundo Deep",
    page_icon="🌟",
    layout="wide"
)
# #Estilo de to
st.markdown("""
<style>

/* Primer contenedor */
.block-container {
    max-width: 1000px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    margin: 0 auto;
}

/* Fondo blanco */
.stApp {
    background-color: #ffffff;
}

/* Hero */
.hero-box {
    background: radial-gradient(circle at top left, #e0f2ff, #f7fbff);
    border-radius: 24px;
    padding: 32px 30px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    margin-bottom: 26px;
}

.hero-title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #102a43;
    margin-bottom: 0.3rem;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: #334e68;
    max-width: 680px;
}

.tag-chip {
    display: inline-block;
    background-color: #dbeafe;
    color: #1d4ed8;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    margin-bottom: 8px;
}

/* Tarjeta explicativa */
.card-explain {
    background: #ffffff;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    padding: 18px 20px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.04);
    margin-bottom: 24px;
    font-size: 0.98rem;
    color: #1f2933;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1f3b5d;
    margin-top: 10px;
    margin-bottom: 6px;
}

.custom-list li {
    margin-bottom: 4px;
}

img {
    border-radius: 18px;
}
/*Las tarjetas de transformers*/
.topic-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 5rem;          /* <-- más espacio horizontal y vertical */
    margin-top: 2.2rem;
    margin-bottom: 2.5rem;
}

/* Tarjeta base: fondo clarito, texto oscuro */
.topic-card {
    width: 260px;
    background: #f9fafb;                       /* fondo gris muy suave */
    border-radius: 18px;
    padding: 18px 18px 16px 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
    text-decoration: none !important;
    display: flex;
    flex-direction: column;
    gap: 8px;
    transition: transform 0.16s ease, box-shadow 0.16s ease, border-color 0.16s ease;
}

/* Variantes de color: borde lateral y fondo un poquito tintado */
.card-transformers {
    background: #e0f2fe;                       /* azul muy suave */
    border-left: 6px solid #3b82f6;
}
.card-callbacks {
    background: #ede9fe;                       /* lila muy suave */
    border-left: 6px solid #a855f7;
}
            
.card-regularizacion {
    background: #F5E6F5;                       /* lila muy suave */
    border-left: 6px solid #FF3DFF;
}

.card-LSTM {
    background: #ECFFEB;                       /* lila muy suave */
    border-left: 6px solid #4AFF3D;
}

.card-rna {
    background: #FFEBEB;                       /* lila muy suave */
    border-left: 6px solid #FF0000;
}
            
.card-perceptron {
    background: #FFFAF2;                       /* lila muy suave */
    border-left: 6px solid #FF8C00;
}
            
.card-embedding {
    background: #F0FFFF;                       /* lila muy suave */
    border-left: 6px solid #00FFFA;
}

/* Cabecera de la tarjeta */
.topic-header {
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Icono redondo */
.topic-icon {
    width: 34px;
    height: 34px;
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
    background: #ffffff55;
}

/* Texto: AHORA ES OSCURO, NO BLANCO */
.topic-title-text {
    font-weight: 700;
    color: #111827;
    font-size: 1.05rem;
}
.topic-desc {
    font-size: 0.9rem;
    color: #374151;
}

.topic-footer {
    font-size: 0.8rem;
    font-weight: 600;
    color: #1d4ed8;
}

/* Hover suave */
.topic-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 26px rgba(15, 23, 42, 0.14);
    border-color: #bfdbfe;
}

/* Quitar subrayado y azul horrible de link */
.topic-card:link,
.topic-card:visited,
.topic-card:hover,
.topic-card:active {
    text-decoration: none !important;
    color: inherit !important;
}

/* Botón volver */
.volver-btn button {
    border-radius: 999px !important;
}

</style>
""", unsafe_allow_html=True)




# ================== NAVEGACIÓN ================== #
params = st.experimental_get_query_params()
page = params.get("page", ["home"])[0]


# ================== HOME ================== #
if page == "home":

    st.markdown("""
    <div class="hero-box">
        <div class="tag-chip">Curso de Deep Learning</div>
        <div class="hero-title">Bienvenidos al Mundo de Deep 🌟</div>
        <div class="hero-subtitle">
                Hola! Acá vas a encontrar algunos temas de deep learning con explicaciones
                sencillas, ejemplos visuales y recursos para que no entres en pánico con este curso.
        </div>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="card-explain">

    <p><b>Pero.. tacho, primero que todo ¿Qué es el Deep Learning?</b></p>

    <p>
        Para "Barajarla" más despacio y que no se agobien, el deep learning es un subcampo de
        la inteligencia artificial que intenta imitar el cerebro humano utilizando redes 
        neuronales con muchas capas para aprender patrones complejos a partir de los datos.
    </p>

    <p>
        Esta es la parte interesante, porque en vez de programar reglas, le mostramos ejemplos:
        Imágenes, texto, audio entre otros, y el modelo aprende a reconocer, traducir, generar
        o predecir cosas por sí solo.
    </p>

    <p>
        Pero esto no pasa por arte de magia (Ojalá). Para lograr esto hay diferentes formas, 
        métodos y herramientas, y esta página está pensada precisamente para que no entren "crudos" a
        esta materia.✨
    </p>

    </div>
    """, unsafe_allow_html=True)



    st.image(
        "assets/images/gatosentado.jpeg",
        caption="Sienténse y tomen nota, vamos a ser como este gato",
        use_container_width=True
    )
 
    st.markdown("""
<div class="card-explain">

<p><b>Ahora sí, hablemos de cómo el Deep Learning intenta imitar nuestro cerebro</b></p>

<p>
    Acá viene la parte chévere: las redes neuronales están inspiradas en las neuronas humanas.
    No es que tengan conciencia (todavía), pero sí copian la idea de que muchas neuronas
    sencillas trabajando juntas pueden aprender cosas complejas.
</p>

<p>
    Eso permite que el deep aprenda patrones que ni nosotros podemos explicar bien:
    reconocer caras, traducir idiomas, detectar tumores, recomendarte qué ver en Netflix,
    escribir textos, decidir si en una foto hay o no hay algo.
</p>


</div>
""", unsafe_allow_html=True)
    
    st.image(
        "assets/images/vacasola.jpeg",
        caption="No todo en la vida es bueno, por eso:",
        use_container_width=True
    )

    st.markdown("""
<div class="card-explain">

<p><b>Peeero… como todo lo bueno en esta vida, tiene su lado misterioso:  La famosa caja negra</b></p>

<p>
    Los modelos a veces aciertan de formas impresionantes y no siempre sabemos exactamente
    qué pasó adentro. No es magia, es matemáticas… pero matemáticas bien profundas.
</p>

<p>
    Eso hace que entender cómo “piensan” sea un reto, pero también lo vuelve un campo fascinante:
    es como estudiar el cerebro… versión digital.
</p>


</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Ya con eso entendido, seguimos ¿Qué encontrarás a continuación?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="custom-list">
        <li>Vas a ver resumenes acerca de lo qué es cada tema</li>
        <li>Tendremos vídeos recomendados, por si quieres saber más y te llamo la atención</li>
        <li>Enlaces a demos y herramientas interactivas en la web para que tu mismo lo modifiques</li>
        <li>Y si hay personas que siempre se preguntan y ¿esto para que me sirve? Acá también te damos la respuesta</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Temas disponibles</div>', unsafe_allow_html=True)
    st.caption("Haz clic en la tarjeta que más te llame la atención y echa un primer vistazo a los temas del curso")

    # ========== TARJETAS DE TEMAS ========== #
    st.markdown('<div class="topic-grid">', unsafe_allow_html=True)

# Perceptrón
    st.markdown(
    """
    <a href="?page=perceptron" class="topic-card card-perceptron">
        <div class="topic-header">
            <div class="topic-icon">⚡</div>
            <div class="topic-title-text">Perceptrón</div>
        </div>
        <div class="topic-desc">
            La neurona artificial más básica: el inicio de las redes neuronales y la base
            para entender cómo "aprende" una sola unidad.
        </div>
        <div class="topic-footer">
            Te interesa? Click acá →
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Transformers
    st.markdown(
        """
        <a href="?page=transformers" class="topic-card card-transformers">
            <div class="topic-header">
                <div class="topic-icon">🐯</div>
                <div class="topic-title-text">Transformers</div>
            </div>
            <div class="topic-desc">
                No, no esos Transformers, acá no hay ningún optimus prime, pero sí
                son los transformers que nos dicen cómo es que los modelos
                entienden el texto completo usando atención y les da vida a herramientas
                que todos utilizamos hoy día como ChatGPT.
            </div>
            <div class="topic-footer">
                ¿Quieres ver este tema? Da click aquí →
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Callbacks
    st.markdown(
        """
        <a href="?page=callbacks" class="topic-card card-callbacks">
            <div class="topic-header">
                <div class="topic-icon">🦁</div>
                <div class="topic-title-text">Callbacks</div>
            </div>
            <div class="topic-desc">
                Acá no vas a llamar a nadie #superar, en esta parte te hablaremos de 
                "trucos" para controlar el entrenamiento: parar a tiempo, guardar el mejor
                modelo, ajustar el learning rate, entre otros.
            </div>
            <div class="topic-footer">
                ¿Te interesa? Click acá →
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Regularización
    st.markdown(
        """
        <a href="?page=regularizacion" class="topic-card card-regularizacion">
            <div class="topic-header">
                <div class="topic-icon">🛡️</div>
                <div class="topic-title-text">Regularización</div>
            </div>
            <div class="topic-desc">
                Aquí aprenderás a ponerle “frenos” a tu red neuronal para que no memorice todo. 
                Veremos técnicas como L1, L2, Dropout y Early Stopping para que tu modelo
                generalice mejor y sea más confiable.
            </div>
            <div class="topic-footer">
                ¿Quieres evitar el overfitting? Click acá →
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )


# LSTM
    st.markdown(
    """
    <a href="?page=LSTM" class="topic-card card-LSTM">
        <div class="topic-header">
            <div class="topic-icon">🌀</div>
            <div class="topic-title-text">LSTM</div>
        </div>
        <div class="topic-desc">
            No, no hablamos de tu memoria a corto plazo cuando olvidas dónde dejaste las llaves. 
            Los LSTM son modelos que —a diferencia de nosotros— sí saben qué recordar y qué olvidar 
            mientras procesan texto paso a paso. Gracias a esa “memoria selectiva inteligente”, 
            dominaron el procesamiento de lenguaje antes de que los Transformers llegaran a robarse el show.
        </div>
        <div class="topic-footer">
            ¿Recuerdas qué desayunaste? El LSTM sí. Explora aquí →
        </div>
    </a>
    """,
    unsafe_allow_html=True
)


    # RNA
    st.markdown(
        """
        <a href="?page=rna" class="topic-card card-rna">
            <div class="topic-header">
                <div class="topic-icon">🦊</div>
                <div class="topic-title-text">RNA</div>
            </div>
            <div class="topic-desc">
                Esta es la parte esencial, aquí se busca procesar datos de una manera
                similar a como lo hace el ser humano. O sea, donde se busca pensar
                como nosotros.
            </div>
            <div class="topic-footer">
                Yo sé que quieres saber más. Click acá →
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Embeddings
    st.markdown(
        """
        <a href="?page=embeddings" class="topic-card card-embedding">
            <div class="topic-header">
                <div class="topic-icon">🐖</div>
                <div class="topic-title-text">Embedding</div>
            </div>
            <div class="topic-desc">
                No, no esas incrustaciones…  
                Porque sí, aunque en español la 
                traducción técnica sea literalmente “incrustaciones”, 
                nadie en su sano juicio piensa en matemáticas cuando oye
                “incrustar algo”.
            </div>
            <div class="topic-footer">
                ¿Incrustar algo? Investiga, click aquí →
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    
    

    # LLM

    st.markdown(
    """
    <a href="?page=llm" class="topic-card card-transformers">
        <div class="topic-header">
            <div class="topic-icon">🧠</div>
            <div class="topic-title-text">LLM</div>
        </div>
        <div class="topic-desc">
            Los modelos de lenguaje gigantes que generan texto, entienden contexto y
            aprenden patrones del lenguaje a gran escala usando transformers.
        </div>
        <div class="topic-footer">
            Te interesa? Click acá →
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ================== PÁGINA: TRANSFORMERS ================== #
elif page == "transformers":
    st.title("🐯 Transformers")
    st.markdown("---")
  
    st.subheader("Listo, ¿de qué transformers estamos hablando?")
    st.markdown("""
Tranqui, acá no vamos a hablar de Optimus Prime ni de Bumblebee.  
Cuando decimos **Transformers** en Deep Learning, hablamos de una arquitectura de red neuronal
que se volvió la estrella del texto (y ahora también de imágenes, audio, etc.)

💡 La idea es: 

- Trabajan con secuencias (palabras, tokens, lo que sea).
- En vez de leer todo de izquierda a derecha sufriendo con la memoria (como las RNN),
- el modelo **ve la secuencia completa al tiempo** y decide a qué partes ponerle más cuidado.

Ese “ponerle cuidado” es lo que se conoce como **auto-atención** (*self-attention*).
    """)
    st.image(
        "assets/images/monopensando.jpeg"
    )

    st.subheader("¿Qué hace exactamente la auto-atención?")
    st.markdown("""
Imagina esta frase:

> "La niña dejó el cuaderno en la mesa porque **estaba** roto."

Tú, cerebro humano aparentemente funcional, sabes que “estaba roto” se refiere al cuaderno,  
no a la mesa ni a la niña.

La atención hace algo parecido:

- cada palabra **mira** a todas las demás
- decide cuáles son más importantes en ese contexto
- les asigna pesos (importancia)
- mezcla toda esa info
- y eso se repite por varias capas.

Así el modelo no solo ve palabras sueltas, sino **relaciones** entre ellas.
Por eso a los Transformers se les da tan bien entender contexto.
    """)

    st.subheader("¿Por qué los Transformers cambiaron el juego?")
    st.image(
        "assets/images/mapache alabando.jpeg"
    )
    st.markdown("""
Antes se usaban RNN y LSTM, que:

- leían la secuencia en orden, una palabra detrás de otra,  
- se cansaban con secuencias largas,  
- y eran más difíciles de paralelizar.

Con los Transformers:

- Se puede **paralelizar** el procesamiento → entrenan mucho más rápido.
- Capturan relaciones de largo alcance (cosas que pasan al inicio de un texto y afectan al final).
- Son la base de modelos como **GPT, BERT, T5, ViT** y en general la mayoría de LLMs modernos.
- Escalan muy bien: más datos + más capas + más parámetros = modelos cada vez más capaces (y tercos).
    """)

    st.subheader("¿Y ajá chévere y todo, pero yyy esto dónde lo veo en la vida real?")
    st.markdown("""
Detrás de cosas como:

- ChatGPT y otros chatbots conversacionales.
- Traductores automáticos que ya no suenan a Google Translator 2010.
- Motores de búsqueda más inteligentes.
- Modelos que generan imágenes y hasta código.

Todo eso corre gracias a algún primo Transformer por ahí trabajando 24/7 (Nadie esta siendo explotado acá).
    """)

    st.subheader("Si son curiosos y quieren entender más, echenle un ojito a estos vídeos/Artículos")
    st.write("Con uno o dos de estos ya agarras muy buena intuición:")

    col1, col2, col3= st.columns(3)
    with col1:
        st.video("https://www.youtube.com/watch?v=Kp4Mvapo5kc")  # Transformers explicado en español
    with col2:
        st.video("https://www.youtube.com/watch?v=zxQyTK8quyY")  # Atención y Transformers
    with col3:
        st.video("https://www.youtube.com/watch?v=eMlx5fFNoYc&t=1105s")
    
    st.markdown("""
-[¿Qué es un transformer?](https://medium.com/inside-machine-learning/what-is-a-transformer-d07dd1fbec04)
                Artículo que explica que son los transformers
                """)
    st.subheader("Quieres verlo en acción por tu cuenta? Estas páginas son perfectas para que juegues con parámetros")
    st.markdown("""
- [Transformer Explainer (visual, interactivo)](https://poloclub.github.io/transformer-explainer/)  
  Puedes ver cómo la atención cambia palabra por palabra.
- [LLM 3D Visualizer](https://bbycroft.net/llm)  
  Una visualización 3D loquísima de cómo se ve un modelo grande por dentro.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)  
  Blog súper visual, cero trauma con ecuaciones.
    """)

    st.subheader("Qué deberías llevarte de este tema (lo mejor siempre para el final)")
    st.markdown("""
- Un Transformer **usa auto-atención** para decidir qué partes del input son relevantes entre sí.  
- No recorre el texto “a la antigua”, sino que **ve todo al tiempo**.  
- Funciona muy bien con texto, pero también se ha adaptado a imágenes, audio y más.  
- Los **LLMs** (como ChatGPT) son básicamente **Transformers gigantes** entrenados para predecir
  el siguiente token muchas, muchas, muchas veces.
    """)
    
    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep ⭐"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)



# ================== PÁGINA: CALLBACKS ================== #
elif page == "callbacks":
    st.title("🐞 Callbacks")
    st.markdown("---")

    st.subheader("¿Qué es un callback en Deep Learning?")
    st.markdown("""
Piensa en un callback como ese amigo que te acompaña al gimnasio y te dice:

> “Vamos, una más, unita... no mentiras terminamos ahí”

o

> “Párele, sufiente día de pierna por hoy (van en la primera serie).”

Un *callback* hace **exactamente eso**, pero durante el entrenamiento de tu modelo.

Mientras el modelo entrena, el callback mira lo que está pasando y toma decisiones inteligentes:
- “Oiga, usted si no cambia, ya no está mejorando → pare.”
- “Uy, esta época quedó mela caramela → guárdela.”
- “Mmm… está estancado, salga de ahí → bájele a la learning rate.”
- “Quiero ver esto en TensorBoard → mándeme logs.”

En pocas palabras:
**son asistentes que mejoran el entrenamiento sin que tú metas mano cada rato.**
    """)

    st.subheader("¿Pero y por qué son útiles?")
    st.markdown("""
Porque entrenar modelos puede ser así:

- empieza súper bien,  
- luego empieza a memorizar cosas que no debería,  
- luego se estanca,  
- luego empieza a improvisar como si fuera artista y alusina durísimo.  

Los callbacks ayudan a:
- evitar el *overfitting*,  
- no perder el mejor modelo,  
- entrenar más rápido,  
- ajustar parámetros automáticamente.  

Sin cambiar arquitectura, sin fórmulas nuevas → solo con un par de “asistentes inteligentes”.
    """)

    st.subheader("Videitos que explican un poco más")
    col1, col2 = st.columns(2)

    with col1:
        st.video("https://www.youtube.com/watch?v=lHkG0uZZ330")  # Explicación simple de callbacks
    with col2:
        st.video("https://www.youtube.com/watch?v=N-1zpHn8xlI")  # EarlyStopping explicado

    st.caption("Ambos muestran los callbacks sin drama matemático.")

    st.subheader("Y claramente si quieren explorar en estas páginas pueden jugar con parametros")
    st.markdown("""
- ⭐ **Simula entrenamiento con EarlyStopping (interactivo):**  
  https://loss-landscape.playground.tensorflow.org/#callback=earlystop  

- ⭐ **Explora cómo afecta la learning rate:**  
  https://poloclub.github.io/nnlosslandscape/  

- ⭐ **TensorBoard demo oficial:**  
  https://tensorboard.dev/  
    """)

    st.subheader("Los callbacks más usados")
    st.markdown("""
**1. EarlyStopping**  
Como el amigo con el que uno esta y le dice "una y no más" o "una y nos vamos" (Pero en este caso es verdad).

**2. ModelCheckpoint**  
El parcero que toma la foto siempre en el momento preciso.

**3. ReduceLROnPlateau**  
El parcero que dice que sean pareja al día de conocerse y uno le dice 
                "vamos más lento".

**4. TensorBoard**  
Este es como el profesor que al final de semestre le va mostrando las notas de como va y el progreso
                (y uno recién se va enterando que va perdiendo y que tiene que salvar el semestre en 1 semana)
    """)

    st.subheader("💡 Mini demo mental")
    st.markdown("""
Imagina entrenar por 50 épocas sin callbacks:

- tu modelo aprende bien y va melo 
- luego se empieza a pasar y sobreaprende y sigue.. y sigue y y y
- luego se daña...

Con callbacks, pasa así:

- aprende bien (va melo) 
- EarlyStopping dice: “epa, ya estuvo bien, no más, deje ahí”  
- ModelCheckpoint dice: “me quedo con la mejor versión, gracias a todos por participar.”  

Simple y efectivo.
    """)

    st.subheader("🔧 Código para no olvidar")
    st.code("""
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

checkpoint = ModelCheckpoint(
    'mejor_modelo.keras',
    monitor='val_loss',
    save_best_only=True
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=32,
    callbacks=[early_stop, checkpoint]
)
""", language="python")

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)

############

elif page == "regularizacion":
    st.title("🛡️ Regularización en Redes Neuronales")
    st.markdown("---")

    st.subheader("¿Qué es la regularización?")
    st.markdown("""
La **regularización** es un conjunto de técnicas que ayudan a que una red neuronal **no se sobreentrene** con los datos de entrenamiento.  
El sobreentrenamiento (**overfitting**) ocurre cuando la red memoriza los datos en lugar de **aprender patrones generales**, lo que hace que falle con datos nuevos.

Piensa en la regularización como un **“freno”** que evita que la red sea demasiado compleja.
    """)

    st.subheader("¿Por qué es importante?")
    st.markdown("""
- Evita que la red aprenda ruido o detalles irrelevantes.  
- Mejora la **capacidad de generalización** a nuevos datos.  
- Hace que el modelo sea más **estable y confiable**.
    """)

    st.subheader("Tipos principales de regularización")
    st.markdown("""
1. **L1 (Lasso)**  
   - Penaliza la suma de los valores absolutos de los pesos.  
   - Favorece que algunos pesos sean exactamente cero, generando un modelo más **simple y escaso**.

2. **L2 (Ridge)**  
   - Penaliza la suma de los cuadrados de los pesos.  
   - Evita que los pesos tomen valores muy grandes, haciendo la red más **suave y estable**.

3. **Dropout**  
   - Durante el entrenamiento, algunas neuronas se **apagan aleatoriamente** en cada iteración.  
   - Esto fuerza a la red a no depender de neuronas específicas, mejorando la **robustez**.

4. **Early Stopping**  
   - Se detiene el entrenamiento cuando el error en el conjunto de validación **deja de mejorar**.  
   - Evita entrenar demasiado tiempo y sobreajustar los datos.
    """)

    st.subheader("Ejemplo de regularización en Keras")
    st.code("""
from tensorflow.keras import layers, models, regularizers

model = models.Sequential([
    layers.Dense(64, activation='relu', 
                 kernel_regularizer=regularizers.l2(0.01),
                 input_shape=(X_train.shape[1],)),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Early stopping
from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(X_train, y_train,
                    epochs=100,
                    batch_size=32,
                    validation_data=(X_valid, y_valid),
                    callbacks=[early_stop])
    """, language="python")

    st.subheader("Tips prácticos")
    st.markdown("""
- Combina **L2 y Dropout** para obtener buena generalización.  
- Ajusta la **tasa de Dropout** entre 0.2 y 0.5 según el tamaño de tu red.  
- Monitorea siempre la **pérdida de validación** para detectar sobreentrenamiento.  
- La regularización no reemplaza la necesidad de **buenos datos**: más y mejores datos siempre ayudan.
    """)

    st.markdown("---")
    st.subheader("Video recomendado")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=Q4Wc2zMYd2U")  # Explicación rápida y clara
    with col2:
        st.video("https://www.youtube.com/watch?v=5tcbyHhsLJk")  # Columna vacía si solo hay un video

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)



    #######################RNA##########################3333
elif page == "rna":
    st.title("🦊 Redes Neuronales Artificiales (RNA)")
    st.markdown("---")

    st.subheader("¿Qué es una RNA?")
    st.markdown("""
Una **Red Neuronal Artificial (RNA)** es un modelo de inteligencia artificial inspirado en cómo funciona
el cerebro humano. Su objetivo es **aprender patrones** a partir de datos y hacer predicciones o clasificaciones.

Piensa en ella como un conjunto de **neuronas artificiales** conectadas, que reciben información,
la procesan y generan una salida.
    """)

    st.subheader("¿Cómo funciona una neurona artificial?")
    st.markdown("""
Cada neurona en la red realiza tres tareas principales:

1. **Recibe entradas**: valores numéricos que representan características de los datos (por ejemplo: edad, ingresos, temperatura).  
2. **Procesa la información**: multiplica cada entrada por un **peso** (qué tan importante es esa entrada), suma un **bias** y aplica una **función de activación** para decidir la salida.  
3. **Entrega un resultado**: que puede enviarse a otras neuronas en capas siguientes o como salida final.

El conjunto de estas neuronas conectadas permite **aprender relaciones complejas** que otros modelos simples no pueden.
    """)

    st.subheader("Funciones de activación")
    st.markdown("""
Las **funciones de activación** permiten que la red aprenda patrones complejos al introducir **no linealidad**:

- **Sigmoide**: valores entre 0 y 1, ideal para clasificación binaria.  
- **ReLU (Rectified Linear Unit)**: devuelve 0 si el valor es negativo y el mismo valor si es positivo. Muy usada en capas ocultas.  
- **Tanh**: valores entre -1 y 1, ayuda a centrar los datos.
    """)

    st.subheader("Aprendizaje: cómo la RNA mejora")
    st.markdown("""
La red **aprende ajustando pesos y bias** para que sus predicciones se acerquen a los resultados correctos:

- **Forward pass**: los datos pasan por la capa de entrada hasta generar la predicción.  
- **Backpropagation**: se calcula el error y se ajustan los pesos hacia atrás para reducirlo.  
- Este proceso se repite muchas veces hasta que la red domina los patrones.
    """)

    st.subheader("Usos prácticos")
    st.markdown("""
Las RNA se usan en muchísimas aplicaciones:

- 🔍 **Clasificación**: riesgo crediticio, spam, diagnóstico médico.  
- 📈 **Regresión**: predicción de precios, ventas o demanda.  
- 🖼️ **Visión por computadora**: reconocimiento facial, detección de objetos.  
- 🗣️ **Procesamiento de lenguaje**: chatbots, traducción automática, análisis de sentimiento.  
- 🎮 **Aprendizaje por refuerzo**: agentes que aprenden a tomar decisiones óptimas.
    """)

    st.subheader("Ejemplo visual en Keras")
    st.code("""
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # clasificación binaria
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train,
                    epochs=50,
                    batch_size=32,
                    validation_data=(X_valid, y_valid))
    """, language="python")

    st.subheader("¿Dónde vemos RNA en la vida real?")
    st.markdown("""
- Chatbots como ChatGPT  
- Reconocimiento facial en tu teléfono  
- Recomendaciones de productos en tiendas online  
- Predicciones médicas y financieras
    """)

    st.markdown("---")
    st.subheader("Videos recomendados")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=jKCQsndqEGQ")  # Buen video, bien explicado
    with col2:
        st.video("https://www.youtube.com/watch?v=Kovwua0Mmp4")  # Columna vacía si solo hay un video

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)

#12323hj3123h21nj3k12hbn2k3h2jk321hjk3

elif page == "regularizacion":
    st.title("🛡️ Regularización en Redes Neuronales")
    st.markdown("---")

    st.subheader("¿Qué es la regularización?")
    st.markdown("""
La **regularización** es un conjunto de técnicas que ayudan a que una red neuronal **no se sobreentrene** con los datos de entrenamiento.  
El sobreentrenamiento (**overfitting**) ocurre cuando la red memoriza los datos en lugar de **aprender patrones generales**, lo que hace que falle con datos nuevos.

Piensa en la regularización como un **“freno”** que evita que la red sea demasiado compleja.
    """)

    st.subheader("¿Por qué es importante?")
    st.markdown("""
- Evita que la red aprenda ruido o detalles irrelevantes.  
- Mejora la **capacidad de generalización** a nuevos datos.  
- Hace que el modelo sea más **estable y confiable**.
    """)

    st.subheader("Tipos principales de regularización")
    st.markdown("""
1. **L1 (Lasso)**  
   - Penaliza la suma de los valores absolutos de los pesos.  
   - Favorece que algunos pesos sean exactamente cero, generando un modelo más **simple y escaso**.

2. **L2 (Ridge)**  
   - Penaliza la suma de los cuadrados de los pesos.  
   - Evita que los pesos tomen valores muy grandes, haciendo la red más **suave y estable**.

3. **Dropout**  
   - Durante el entrenamiento, algunas neuronas se **apagan aleatoriamente** en cada iteración.  
   - Esto fuerza a la red a no depender de neuronas específicas, mejorando la **robustez**.

4. **Early Stopping**  
   - Se detiene el entrenamiento cuando el error en el conjunto de validación **deja de mejorar**.  
   - Evita entrenar demasiado tiempo y sobreajustar los datos.
    """)

    st.subheader("Ejemplo de regularización en Keras")
    st.code("""
from tensorflow.keras import layers, models, regularizers

model = models.Sequential([
    layers.Dense(64, activation='relu', 
                 kernel_regularizer=regularizers.l2(0.01),
                 input_shape=(X_train.shape[1],)),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Early stopping
from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(X_train, y_train,
                    epochs=100,
                    batch_size=32,
                    validation_data=(X_valid, y_valid),
                    callbacks=[early_stop])
    """, language="python")

    st.subheader("Tips prácticos")
    st.markdown("""
- Combina **L2 y Dropout** para obtener buena generalización.  
- Ajusta la **tasa de Dropout** entre 0.2 y 0.5 según el tamaño de tu red.  
- Monitorea siempre la **pérdida de validación** para detectar sobreentrenamiento.  
- La regularización no reemplaza la necesidad de **buenos datos**: más y mejores datos siempre ayudan.
    """)

    st.markdown("---")
    st.subheader("Video recomendado")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=Kovwua0Mmp4")  # Explicación rápida y clara
    with col2:
        st.write("")  # Columna vacía si solo hay un video

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)



# ================== PÁGINA: Embbeddings ================== #

elif page == "embeddings":
    st.title("🐖 Embeddings")
    st.markdown("---")

    st.subheader("Antes que nada… ¿embeddings? ¿Incrustaciones?")
    st.markdown("""
Sí, en español suena rarísimo: *“incrustaciones semánticas”*.  
La primera vez que uno ve ese subtítulo piensa que esto va de joyería y no de Deep Learning.

Pero no: un **embedding** es simplemente una forma inteligente de representar palabras como **vectores** 
que capturan *su significado*.  
Es el puente entre lenguaje humano → matemáticas.
    """)

    st.subheader("¿Por qué existen los embeddings?")
    st.markdown("""
Antes del boom de NLP moderno usábamos:

### One-Hot Encoding  
- Vectores gigantes llenos de ceros.  
- Cada palabra = un vector sin lógica semántica.  
- “perro” y “gato” son tan distintos como “perro” y “wifi”.

### Bag-of-Words  
- Cuenta palabras pero ignora orden y significado.

Estos métodos no entienden **relaciones**.  
Ahí es donde entran los embeddings.
    """)

    st.subheader("Embeddings: la idea corta")
    st.markdown("""
Los embeddings crean un **mapa semántico** donde:

- “rey” y “reina” quedan cerca.  
- “perro”, “perrito”, “canino” también.  
- Las palabras raras o nuevas siguen teniendo representación (FastText).  
- Cada vector captura relaciones reales del lenguaje.

Representan significado, no solo frecuencia.
    """)

    st.markdown("---")
    st.subheader("Tipos de embeddings (versión comprimida)")

    st.markdown("###1. **Embeddings No Contextuales** (vectores fijos por palabra)")
    st.markdown("""
Estos modelos producen **un solo vector por palabra**, sin importar la frase donde aparezca.

| Modelo | Tipo | Entrada | Objetivo |
|--------|------|---------|----------|
| **CBOW** | Predictivo | Palabras del contexto | Predecir la palabra central |
| **Skip-Gram** | Predictivo | Una palabra central | Predecir palabras del contexto |
| **FastText** | Predictivo con sub-palabras | n-gramas + palabra | Predecir contexto (mejor con palabras nuevas) |
| **GloVe** | Conteo + factorización | Coocurrencias globales | Factorizar matriz para obtener vectores |

> `"banco"` tendrá el **mismo vector** en: “me senté en el banco” y “fui al banco”.
    """)

    st.markdown("###**Embeddings Contextuales** (vectores que cambian según la frase)")
    st.markdown("""
Aquí la misma palabra tiene **vectores distintos** según el contexto.

| Modelo | Red | Objetivo | ¿Contextual? |
|--------|-----|----------|--------------|
| **ELMo** | LSTM | Modelo de lenguaje | ✅ |
| **BERT** | Transformer | Palabras enmascaradas | ✅ |
| **GPT** | Transformer | Siguiente palabra | ✅ |

> `"banco"` sí cambia si hablas de dinero o de sentarte.
    """)

    st.markdown("---")
    st.subheader("CBOW vs Skip-Gram vs FastText (versión práctica)")

    st.markdown("""
| Tarea | Mejor método | Por qué |
|-------|--------------|----------|
| Conceptos similares | **CBOW** | Estable y rápido |
| Relaciones semánticas complejas | **Skip-Gram** | Mejor en matices |
| Palabras nuevas / errores | **FastText** | Usa sub-palabras |
| Frases similares | **Skip-Gram** | Mayor recall |
    """)

    st.markdown("---")
    st.subheader("Embeddings más usados en la vida real")
    st.markdown("""
- **Word2Vec (CBOW / Skip-Gram)** → clásico y rápido.  
- **FastText** → entiende sub-palabras.  
- **GloVe** → basado en coocurrencias globales.  
- **ELMo** → contextual con LSTM.  
- **BERT embeddings** → estándar moderno.  
- **Sentence Transformers (SBERT)** → para búsquedas, QA, similitud de frases.
    """)

    st.markdown("---")
    st.subheader("Videos recomendados")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://youtu.be/my5wFNQpFO0")  # Intuición
    with col2:
        st.video("https://youtu.be/hVM8qGRTaOA")  # Explicación detallada

    st.markdown("---")
    st.subheader("Ahora probemos 🧪 (Similitud del coseno con GloVe)")

    st.markdown("""
Aquí puedes cargar dos palabras y comparar sus **embeddings de GloVe**  
para ver qué tan parecidas son matemáticamente.
    """)

    # --- INTERACTIVE DEMO ---

    import os
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity

    @st.cache_resource
    def load_glove():
        embedding_index = {}
        glove_path = "glove.6B.50d.txt"
        if os.path.exists(glove_path):
            with open(glove_path, encoding="utf-8") as f:
                for line in f:
                    values = line.split()
                    word = values[0]
                    vector = np.asarray(values[1:], dtype="float32")
                    embedding_index[word] = vector
        return embedding_index

    embedding_index = load_glove()

    st.success(f"Embeddings cargados: {len(embedding_index)} palabras disponibles.")

    st.markdown("### Elige dos palabras para comparar:")
    colA, colB = st.columns(2)
    with colA:
        word1 = st.text_input("Primera palabra:", "king")
    with colB:
        word2 = st.text_input("Segunda palabra:", "queen")

    def get_vector(word):
        return embedding_index.get(word.lower(), None)

    if st.button("🔍 Calcular similitud del coseno"):
        vec1 = get_vector(word1)
        vec2 = get_vector(word2)

        if vec1 is None:
            st.error(f"La palabra **{word1}** no existe en los embeddings.")
        elif vec2 is None:
            st.error(f"La palabra **{word2}** no existe en los embeddings.")
        else:
            similarity = cosine_similarity([vec1], [vec2])[0][0]

            st.markdown("### Resultados")
            st.write(f"**Vector de `{word1}`:**")
            st.code(vec1)

            st.write(f"**Vector de `{word2}`:**")
            st.code(vec2)

            st.metric(
                label=f"Similitud del coseno entre '{word1}' y '{word2}'",
                value=f"{similarity:.4f}"
            )

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== PÁGINA: LLMS ================== #
elif page == "llm":
    st.title("🧠 LLMs")
    st.markdown("---")

    st.subheader("¿Qué es un LLM?")
    st.markdown("""
Un **LLM (Large Language Model)** es un modelo de deep learning entrenado para trabajar con lenguaje natural.
Su objetivo es simple de describir:

> “Dado un texto, predice cuál debería ser el siguiente token.”

Esa tarea, repetida millones de veces con enormes cantidades de datos, permite que los LLMs:
- escriban textos coherentes,
- respondan preguntas,
- traduzcan,
- resuman,
- generen código,
- mantengan conversaciones,
- y entiendan contexto de formas muy avanzadas.

Los LLMs funcionan gracias a una arquitectura: **los Transformers**, la base de casi todos los modelos modernos.
    """)

    st.subheader("¿Cómo funciona un LLM por dentro?")
    st.markdown("""
1. **Tokenización**  
   El texto se divide en tokens (pedacitos optimizados, no palabras completas).

2. **Embeddings**  
   Cada token se convierte en un vector que representa su significado en un espacio matemático.

3. **Capas de Transformer**  
   El modelo usa **auto-atención** para encontrar relaciones entre tokens y entender contexto.

4. **Predicción autoregresiva**  
   El modelo predice el siguiente token, lo agrega a la secuencia… y repite.

Así generan texto, paso a paso.
    """)

    st.subheader("¿Qué hace que los LLMs funcionen tan bien?")
    st.markdown("""
- Se entrenan con cantidades enormes de datos.  
- Tienen millones o miles de millones de parámetros.  
- Capturan patrones y estructuras del lenguaje.  
- Escalan increíblemente bien: mientras más grandes, mejor funcionan.
    """)

    st.subheader("Vídeos recomendados")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=MR7Dkyc7WSM")
    with col2:
        st.video("https://www.youtube.com/watch?v=wjZofJX0v4M&t=293s")

    st.subheader("Ejemplo en código (Hugging Face Transformers)")
    st.code("""
from transformers import pipeline

# Crear un generador de texto con un modelo pre-entrenado
generator = pipeline("text-generation", model="gpt2")

salida = generator("Un LLM es un modelo que puede", max_length=40)
print(salida[0]['generated_text'])
    """, language="python")

    st.subheader("Intuición rápida")
    st.markdown("""
- Un LLM no “piensa”: **predice tokens**.  
- Aprende a partir de ejemplos, no reglas explícitas.  
- Los Transformers son su cerebro principal.  
- ChatGPT, Gemini, Claude, Llama… todos son LLMs gigantes.  
    """)

    st.markdown("""
¿Sabías que un LLM nunca pierde en piedra, papel o tijera?

Porque **ya predijo** lo que ibas a sacar.  
*(Y si pierde dice que fue por “overfitting emocional”)* 😌
    """)

    st.subheader("Explora más")
    st.markdown("""
Si quieres jugar con uno directamente (sé que lo conoces):

👉 **[Tenemos que hablar...](https://chat.openai.com)**

Allá puedes hacer lo mismo que aquí, pero con más poder, más contexto y menos chistes de estadística  
(o más, depende del día).
    """)

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== PÁGINA: PERCEPTRON ================== #
elif page == "perceptron":
    st.title("⚡ Perceptrón")
    st.markdown("---")

    st.subheader("¿Qué es un perceptrón?")
    st.markdown("""
El **perceptrón** es la unidad más básica de una red neuronal.  
En términos prácticos:

> “Es una neurona artificial que toma entradas, las multiplica por pesos, suma un sesgo, aplica una función de activación y decide entre 0 y 1.”

Su meta principal es aprender a separar datos mediante una **línea recta** (o un plano si hay más dimensiones).  
Eso sí: solo funciona si los datos son **linealmente separables**.
    """)

    st.subheader("¿Cómo funciona?")
    st.markdown("""
Un perceptrón sigue cuatro pasos:

1. **Multiplicación**: cada entrada × su peso  
2. **Suma**: se agrega el sesgo (*bias*)  
3. **Activación**: normalmente una función escalón  
4. **Predicción**: produce 0 o 1  

Es simple, pero es literalmente la base de TODAS las redes neuronales modernas.
    """)

    st.subheader("Ejemplo en código (Perceptrón clásico)")
    st.code("""
import numpy as np

def activacion(x):
    return 1 if x >= 0 else 0

def entrenar(X, y, lr=0.1, epocas=10):
    pesos = np.zeros(X.shape[1])
    bias = 0

    for _ in range(epocas):
        for xi, yi in zip(X, y):
            salida = activacion(np.dot(xi, pesos) + bias)
            error = yi - salida
            pesos += lr * error * xi
            bias += lr * error
    return pesos, bias

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,1])  # OR

pesos, bias = entrenar(X, y)
print("Pesos:", pesos, "Bias:", bias)
    """, language="python")

    st.subheader("Chiste (porque sin chiste no cuenta 😌)")
    st.markdown("""
Un perceptrón entra a un bar.  
El mesero le pregunta:

— ¿Va a pedir algo?  
— Depende del *threshold*.  
*(Si no entendiste, no te preocupes: al perceptrón a veces tampoco le da la activación)* 😎
    """)
    st.subheader("Videos recomendados")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=e9JYMng977Q")  # Perceptrón básico
    with col2:
        st.video("https://www.youtube.com/watch?v=pCy4yPzcCqs&t=77s&pp=ygUbcXXDqSBlcyB1biBwZXJjZXB0cm9uIGVuIG1s")  # OR, AND, XOR explicado visualmente

    st.subheader("Intuición rápida")
    st.markdown("""
- Es la unidad fundamental de una red neuronal  
- Aprende ajustando pesos y sesgos  
- Solo separa datos lineales  
- Es el precursor directo de las *Dense Layers* actuales  
    """)

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")
    st.markdown('</div>', unsafe_allow_html=True)


# ================== PÁGINA: LSTM ================== #

elif page == "LSTM":
    st.title("🧠 LSTM (Long Short-Term Memory)")
    st.markdown("---")

    st.subheader("Listo, ¿qué es exactamente una LSTM?")
    st.markdown("""
No, no estamos hablando de tu memoria a corto plazo cuando olvidas dónde dejaste las llaves.  
Las **LSTM** son redes que, a diferencia de nosotros, sí saben qué recordar y qué olvidar  
mientras procesan texto paso a paso.  
Esa “memoria selectiva inteligente” las hizo famosas mucho antes del reinado de los Transformers.
    """)

    st.subheader("Entonces… ¿qué problema resolvieron las LSTM?")
    st.markdown("""
Antes de las LSTM teníamos las **RNN clásicas**, que intentaban recordar información secuencial.  
El problema era que se les **olvidaban cosas importantes** cuando la secuencia era larga  
o se confundían con detalles irrelevantes.

Las LSTM introdujeron algo revolucionario:

**Un mecanismo interno capaz de decidir qué recordar, qué olvidar y qué usar.**

Esa es la verdadera innovación.  
    """)

    st.subheader("La idea humana detrás de las compuertas de una LSTM")
    st.markdown("""
Piensa en una LSTM como un amigo que escucha tu historia y tiene una memoria selectiva muy fina:
solo guarda lo que importa y descarta lo irrelevante.

Para lograrlo, usa **tres compuertas** y un estado interno:

---

### 🚪1. *Compuerta de olvido* — “¿Qué parte del pasado vale la pena guardar?”
Decide qué fracción de lo que venía antes **se conserva (≈1)**  
y qué fracción **se elimina (≈0)**.

Es la que permite que la red **no se quede pegada a información obsoleta**.

---

### 📝2. *Compuerta de entrada + candidatos* — “¿Qué nueva info debería añadir?”
- La compuerta de entrada decide **dónde** escribir.  
- Los candidatos proponen **qué** podríamos almacenar si vale la pena.

Esto evita que la red agregue ruido o datos innecesarios.

---

### 🧱3. *Actualización del estado de la celda* — “Construyamos la nueva memoria”
Aquí se mezcla:
- lo que sobrevivió del pasado (olvido),  
- con lo que se aprobó del presente (entrada).

Es la **memoria larga** de la LSTM.

---

### 🔎4. *Compuerta de salida* — “¿Qué parte de la memoria mostramos al exterior?”
Decide qué parte del estado interno se expone.  
Luego aplica una especie de filtro suave (tanh) para que no se salga de control.

Ese resultado es lo que se pasa a la siguiente capa/tiempo.

---

En resumen:

> Las compuertas son filtros inteligentes que mantienen la memoria útil,  
> descartan basura y permiten usar la información correcta en el momento adecuado.
    """)

    st.subheader("¿Y en qué mejora esto frente a otros modelos?")
    st.markdown("""
Comparado con modelos previos, una LSTM:

- **supera el olvido rápido** de las RNN tradicionales,  
- maneja secuencias más largas,  
- tiene memoria de largo y corto plazo,  
- evita que los gradientes se destruyan (el famoso *vanishing gradient*),  
- y funciona muy bien en tareas donde **el orden importa**.

### 🆚 Comparación rápida

- **RNN clásica:** recuerda poco, se confunde rápido.  
- **LSTM:** recuerda lo importante con filtros inteligentes.  
- **GRU:** versión simplificada, más rápida y casi igual de buena.  
- **Transformers:** ven todo al tiempo, sin memoria recurrente.

Aun así, las LSTM siguen siendo muy útiles cuando quieres modelos pequeños, ligeros o cuando la secuencia **sí depende del paso anterior**.
    """)

    st.subheader("¿Dónde se usan en la vida real?")
    st.markdown("""
- Modelos de texto tradicionales  
- Predicción de series temporales  
- Clasificación de sentimiento  
- Procesamiento secuencial donde importa el orden  
- Aplicaciones en voz y audio

Antes del boom de Transformers, las LSTM eran las reinas absolutas del NLP.
    """)

    st.subheader("Videos recomendados (modo visual activado)")
    st.write("Con estos dos videos entiendes la intuición y el funcionamiento interno:")

    col1, col2 = st.columns(2)
    with col1:
        st.video("https://youtu.be/1BubAvTVBYs")  # Intuición LSTM
    with col2:
        st.video("https://youtu.be/8HyCNIVRbSU")  # Explicación completa LSTM/GRU

    st.subheader("Qué deberías llevarte de este tema (versión resumen)")
    st.markdown("""
- Una LSTM decide **qué recordar, qué olvidar y qué usar** mediante compuertas inteligentes.  
- Fue creada para resolver el problema de **memoria corta** de las RNN clásicas.  
- Funciona muy bien con secuencias largas.  
- Las **GRU** son hermanas simplificadas de las LSTM.  
- Aunque los Transformers dominan hoy, las LSTM siguen siendo muy útiles en muchos escenarios.
    """)

    st.markdown("---")
    st.markdown('<div class="volver-btn">', unsafe_allow_html=True)
    if st.button("⬅ Volver a Mundo Deep"):
        st.experimental_set_query_params(page="home")

    st.markdown('</div>', unsafe_allow_html=True)

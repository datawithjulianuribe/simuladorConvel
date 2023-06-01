import dash
import math
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(children=[
    html.H1(['Simulador de presupuesto de proyectos de construcción CONVEL'], id='title',
            style={'textAlign': 'center', 'backgroundColor': 'DarkGray'}),
    html.Br(),
    dcc.Tabs([
        dcc.Tab(label='Acerca de la aplicación', children=[
            dcc.Markdown('''
            En el contexto de cualquier organización, los administradores centran sus esfuerzos en conocer el estado 
            futuro de sus áreas, con el fin de minimizar los riesgos y tomar mejores decisiones. 
            Actualmente, las organizaciones se han centrado en entender y dar valor a los datos generados al interior 
            de sus procesos, mediante el uso de modelos de optimización y herramientas computacionales, con el objetivo
            de convertirlos en información valiosa y encontrar soluciones óptimas y competitivas. 
            El simulador presentado cuenta con el siguiente módulo:
            * La pestaña __*'Simulador presupuesto CONVEL'*__ calcula el precio en metros cuadrados de un proyecto con 
            base en 24 variables claves:
            ''', style={'fontsize': 70, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}),
            html.Div(
                dcc.Markdown('''
                * Estrato (1-2-3-4-5-6)
                * Pisos por torre
                * Pisos por sotano
                * Número de torres
                * Área del Lote en metros cuadrados
                * Área construida total en metros cuadrados
                * Área construida plataforma en metros cuadrados
                * Área huella del edificio en metros cuadrados
                * Cronograma en meses
                * Tipo de suelo {'Flujos':1, 'Arcillas':2, 'Sin dato':3, 'Limos':4, 'Roca':5}
                * Tipo de cimentación {'Pilas':1, 'Pilotes Hincados':2, 'Zapatas':3, 'Pilote Preexcavado':4, 
                'Pilotes':5, 'Pilotes Incados':6, 'Micropilotes':7}
                * Profundidad de cimentación en metros
                * Contenciones en metros cuadrados
                * Estructura {'Aporticada':1, 'Muros Vaciados':2}
                * Preliminares $
                * Excavaciones $
                * Cimentaciones $
                * Mesones $
                * Equipos Especiales $
                * Jardinería $
                * Señalización $
                * Urbanismo $
                * Imprevistos $
                * Honorarios $
             '''), style={'fontsize': 70, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}
            ),
            html.Br(),
            html.Div(
                html.H6('Desarrollado por: Julián Alberto Uribe Gómez. Correo: julian.uribego@gmail.com'),
                style={'fontsize': 52, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}
            ),
            html.Br(),
            html.Div(   
                html.H6('Protegido Dirección Nacional de Derechos de Autor. Colombia. Número de registro: xx-xx-xxx'),
                style={'fontsize': 52, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}
            ),
        ]),
        dcc.Tab(label='Simulador presupuesto CONVEL', children=[
            dcc.Markdown('''
            __*Instrucciones:*__
            La calculadora/simulador tiene como objetivo apoyar el proceso de toma de decisiones al momento establecer
            el precio en metros cuadrados de un proyecto de construcción, para ello se han generado una serie de 
            preguntas que guiarán y ayudarán en el proceso de simulación. 
            Antes de iniciar tenga en cuenta lo siguiente: 
            ''', style={'fontsize': 52, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}),
            html.Div(
                dcc.Markdown('''
                * Responda todas las preguntas.
                * Solo responda con números positivos y no asigne letras, simbolos o caracteres especiales a las 
                casillas de respuesta.
                * Para las variables Tipo de suelo, Tipo de cimentación y Estructura, su equivalente numérico se
                encuentra en la pestaña __*'Acerca de la aplicación'*__.
                * En caso de responder con números decimales o flotantes, utilice punto (.).
                * Puede cambiar cualquier valor para simular el resultado.
                * Se presenta una breve explicación para facilitar la interpretación del valor a ingresar.
                '''), style={'fontsize': 52, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H5('Estrato, pisos y torres del proyecto',
                            style={'textAlign': 'center', 'backgroundColor': 'Gainsboro'}),
                    dcc.Markdown('''
                    1.Estrato donde se construirá el proyecto.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "40px",
                        'text-align': 'center',
                        "margin-right": "40px"
                    }
                                 ),
                    dcc.Input(id='estrato',
                              placeholder='¿Cuál es el estrato donde se construirá el proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    2.Número de pisos por torre.
                    ''', style={'fontsize': 52, "margin-left": "40px", 'text-align': 'center', "margin-right": "40px"}),
                    dcc.Input(id='pisosTorre',
                              placeholder='¿Cuál es la cantidad de pisos por torre que tendrá este proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    3.Número de pisos por sotano.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='pisosSotano',
                              placeholder='¿Cuál es la cantidad de pisos por sotano que tendrá este proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    4.Número de torres en el proyecto.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='torres',
                              placeholder='¿Cuantas torres tendrá este proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                ],
                style={'display': 'block', 'justifyContent': 'center', 'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H5('Sobre las áreas del proyecto.',
                            style={
                                'textAlign': 'center',
                                'backgroundColor': 'Gainsboro'
                            }
                            ),
                    dcc.Markdown('''
                    5.Área del Lote.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='areaLote',
                              placeholder='¿Cuál es el área del lote del proyecto en m2?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    6.Área construida total.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='areaTotal',
                              placeholder='¿Cuál es el área construida total para el proyecto en m2?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    7.Área construida plataforma.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='areaPlataforma',
                              placeholder='¿Cuál es el área construida de plataforma para el proyecto en m2?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    8.Área huella edificio.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='areaHuella',
                              placeholder='¿Cuál es el área huella del edificio para el proyecto en m2?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    9.Cronograma.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='crono',
                              placeholder='¿Cuál es el cronograma del proyecto en meses?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}), 
                ],
                style={'display': 'block', 'justifyContent': 'center', 'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H5('Sobre las cimentaciones y la estructura',
                            style={'textAlign': 'center', 'backgroundColor': 'Gainsboro'}),
                    dcc.Markdown('''
                    10.Tipo de suelo.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='suelo',
                              placeholder='¿Cuál es el tipo de suelo del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    11.Tipo de cimentación.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='tipoC',
                              placeholder='¿Cuál es el tipo de cimentación que tiene el proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    12.Profundidad de cimentación.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='profundidadC',
                              placeholder='¿Cuál es la profundidad de cimentación del proyecto en metros?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    13.Contenciones.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='contencion',
                              placeholder='¿Qué contenciones tendrá el proyecto en m2?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    14.Estructura.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='estructura',
                              placeholder='¿Qué tipo de estructura tendrá el proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                ],
                style={'display': 'block', 'justifyContent': 'center', 'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H5('Sobre los capítulos',
                            style={'textAlign': 'center', 'backgroundColor': 'Gainsboro'}),
                    dcc.Markdown('''
                    15.Preliminares.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='preliminares',
                              placeholder='¿Cuál es el valor de los preliminares - provisionales del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    16.Excavaciones.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='excavaciones',
                              placeholder='¿Cuál es el valor de las excavaciones del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    17.Cimentaciones.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='cimentaciones',
                              placeholder='¿Cuál es el valor de las cimentaciones del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    18.Mesones.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='mesones',
                              placeholder='¿Cuál es el valor de los mesones del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    19.Equipos especiales.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='equipose',
                              placeholder='¿Cuál es el valor de los equipos especiales del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    20.Jardinería.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='jardineria',
                              placeholder='¿Cuál es el valor de la jardinería del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    21.Señalización.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='senalizacion',
                              placeholder='¿Cuál es el valor de la señalización del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    22.Urbanismo.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='urbanismo',
                              placeholder='¿Cuál es el valor del urbanismo del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    23.Imprevistos.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='imprevisto',
                              placeholder='¿Cuál es el valor de los imprevistos del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                    html.Br(),
                    html.Br(),
                    dcc.Markdown('''
                    24.Honorarios.
                    ''', style={
                        'fontsize': 52,
                        "margin-left": "200px",
                        'text-align': 'center',
                        "margin-right": "200px"
                    }
                                 ),
                    dcc.Input(id='honorarios',
                              placeholder='¿Cuál es el valor de los honorarios del proyecto?',
                              type='number',
                              style={'width': '50%', 'justifyContent': 'center', 'textAlign': 'center'}),
                ],
                style={'display': 'block', 'justifyContent': 'center', 'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H5('Resultados', style={'textAlign': 'center', 'backgroundColor': 'Gainsboro'}),
                    html.H5('Precio por metros cuadrados del proyecto simulado'),
                    html.Div(id='output'),
                    html.Br(),
                ],
                style={'fontsize': 60, 'display': 'block', 'justifyContent': 'center', 'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H5('Resultados', style={'textAlign': 'center', 'backgroundColor': 'Gainsboro'}),
                    html.H5('Valor total del proyecto simulado'),
                    html.Div(id='output1'),
                    html.Br(),
                ],
                style={'fontsize': 60, 'display': 'block', 'justifyContent': 'center', 'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                children=[
                    html.H6('Módulo desarrollado por: Julián Alberto Uribe Gómez. Correo: julian.uribego@gmail.com'),
                    html.H6('Ante cualquier duda o sugerencia contacte al autor al correo suministrado.'),
                    html.H6('Protegido Dirección Nacional de Derechos de Autor. Colombia. '
                            'Número de registro: xx-xx-xxx'
                            ),
                ],
                style={'fontsize': 52, "margin-left": "40px", 'text-align': 'justify', "margin-right": "40px"}
            ),
        ]),
    ]),
    
 ], 
 id='layout')


@app.callback(
    Output(component_id='output', component_property='children'),
    [
        Input(component_id='estrato', component_property='value'),
        Input(component_id='pisosTorre', component_property='value'),
        Input(component_id='pisosSotano', component_property='value'),
        Input(component_id='torres', component_property='value'),
        Input(component_id='areaLote', component_property='value'),
        Input(component_id='areaTotal', component_property='value'),
        Input(component_id='areaPlataforma', component_property='value'),
        Input(component_id='areaHuella', component_property='value'),
        Input(component_id='crono', component_property='value'),
        Input(component_id='suelo', component_property='value'),
        Input(component_id='tipoC', component_property='value'),
        Input(component_id='profundidadC', component_property='value'),
        Input(component_id='contencion', component_property='value'),
        Input(component_id='estructura', component_property='value'),
        Input(component_id='preliminares', component_property='value'),
        Input(component_id='excavaciones', component_property='value'),
        Input(component_id='cimentaciones', component_property='value'),
        Input(component_id='mesones', component_property='value'),
        Input(component_id='equipose', component_property='value'),
        Input(component_id='jardineria', component_property='value'),
        Input(component_id='senalizacion', component_property='value'),
        Input(component_id='urbanismo', component_property='value'),
        Input(component_id='imprevisto', component_property='value'),
        Input(component_id='honorarios', component_property='value'),
    ]
)

def proyecto(estrato, pisosTorre, pisosSotano, torres, areaLote, areaTotal, areaPlataforma, areaHuella, crono, suelo,
             tipoC, profundidadC, contencion, estructura, preliminares, excavaciones, cimentaciones, mesones,
             equipose, jardineria, senalizacion, urbanismo, imprevisto, honorarios):

    diccionario = {
        'PrecioM2': {'mean': 1896933.9719233178, 'std': 901625.9632578358},
        'Estrato': {'mean': 4.714285714285714, 'std': 1.3012000972647109},
        'NumeroPisosTorre': {'mean': 19.107142857142858, 'std': 9.585248255886967},
        'NumeroPisosSotano': {'mean': 1.75, 'std': 1.838376900863811},
        'NumeroTorres': {'mean': 2.2142857142857144, 'std': 2.024976320979853},
        'AreaLote': {'mean': 5766.307114285714, 'std': 6721.872963420514},
        'AreaConstruidaTotal': {'mean': 27771.843363773896, 'std': 21570.469577404332},
        'AreaConstruidaPlataforma': {'mean': 5351.982649488183, 'std': 4999.76528369539},
        'AreaHuellaEdificio': {'mean': 1789.925542857143, 'std': 1204.7962558952552},
        'Cronograma': {'mean': 24.821428571428573, 'std': 11.658897639995565},
        'TipoSuelo2': {'mean': 3.0714285714285716, 'std': 0.7163989902474133},
        'TipoCimentacion': {'mean': 2.6785714285714284, 'std': 1.9255316039140873},
        'ProfundidadCimentacion': {'mean': 24.5, 'std': 17.14264770595168},
        'Contenciones': {'mean': 1211.0209142857143, 'std': 3654.756584110812},
        'Estructura': {'mean': 1.3571428571428572, 'std': 0.4879500364742666},
        'V41': {'mean': 766439887.5337161, 'std': 718379380.8302376},
        'V42': {'mean': 787727386.2548462, 'std': 753825614.3828982},
        'V43': {'mean': 5047628856.588471, 'std': 6262799196.36075},
        'V60': {'mean': 233804705.14498094, 'std': 253978737.78937358},
        'V61': {'mean': 2263476282.524756, 'std': 3216303104.1975584},
        'V62': {'mean': 72536181.20438765, 'std': 118342425.75546543},
        'V64': {'mean': 37928530.24276825, 'std': 49929559.82181508},
        'V65': {'mean': 562222416.0000079, 'std': 687696473.5334331},
        'V69': {'mean': 978914670.0439892, 'std': 1126599327.274594},
        'V70': {'mean': 433881020.43211174, 'std': 1038924332.4337287}
    }

    estrato_est = (estrato-diccionario['Estrato']['mean'])/diccionario['Estrato']['std']
    pisosTorre_est = (pisosTorre-diccionario['NumeroPisosTorre']['mean'])/diccionario['NumeroPisosTorre']['std']
    pisosSotano_est = (pisosSotano-diccionario['NumeroPisosSotano']['mean'])/diccionario['NumeroPisosSotano']['std']
    torres_est = (torres-diccionario['NumeroTorres']['mean'])/diccionario['NumeroTorres']['std']
    areaLote_est = (areaLote-diccionario['AreaLote']['mean'])/diccionario['AreaLote']['std']
    areaTotal_est = (areaTotal-diccionario['AreaConstruidaTotal']['mean'])/diccionario['AreaConstruidaTotal']['std']
    areaPlataforma_est = (areaPlataforma-diccionario['AreaConstruidaPlataforma']['mean'])/diccionario['AreaConstruidaPlataforma']['std']
    areaHuella_est = (areaHuella-diccionario['AreaHuellaEdificio']['mean'])/diccionario['AreaHuellaEdificio']['std']
    crono_est = (crono-diccionario['Cronograma']['mean'])/diccionario['Cronograma']['std']
    suelo_est = (suelo-diccionario['TipoSuelo2']['mean'])/diccionario['TipoSuelo2']['std']
    tipoC_est = (tipoC-diccionario['TipoCimentacion']['mean'])/diccionario['TipoCimentacion']['std']
    profundidadC_est = (profundidadC-diccionario['ProfundidadCimentacion']['mean'])/diccionario['ProfundidadCimentacion']['std']
    contencion_est = (contencion-diccionario['Contenciones']['mean'])/diccionario['Contenciones']['std']
    estructura_est = (estructura-diccionario['Estructura']['mean'])/diccionario['Estructura']['std']
    preliminares_est = (preliminares-diccionario['V41']['mean'])/diccionario['V41']['std']
    excavaciones_est = (excavaciones-diccionario['V42']['mean'])/diccionario['V42']['std']
    cimentaciones_est = (cimentaciones-diccionario['V43']['mean'])/diccionario['V43']['std']
    mesones_est = (mesones-diccionario['V60']['mean'])/diccionario['V60']['std']
    equipose_est = (equipose-diccionario['V61']['mean'])/diccionario['V61']['std']
    jardineria_est = (jardineria-diccionario['V62']['mean'])/diccionario['V62']['std']
    senalizacion_est = (senalizacion-diccionario['V64']['mean'])/diccionario['V64']['std']
    urbanismo_est = (urbanismo-diccionario['V65']['mean'])/diccionario['V65']['std']
    imprevisto_est = (imprevisto-diccionario['V69']['mean'])/diccionario['V69']['std']
    honorarios_est = (honorarios-diccionario['V70']['mean'])/diccionario['V70']['std']

    preciom2_est = 1.249e-16 + 0.3613*estrato_est - 0.6360*pisosTorre_est - 0.0450*pisosSotano_est + 0.3270*torres_est \
                   - 0.0138*areaLote_est - 0.1343*areaTotal_est - 0.0334*areaPlataforma_est - 0.2225*areaHuella_est \
                   - 0.2072*crono_est - 0.0828*suelo_est - 0.3671*tipoC_est + 0.1935*profundidadC_est \
                   + 0.5486*contencion_est + 0.0147*estructura_est + 1.1503*preliminares_est - 0.1596*excavaciones_est \
                   + 0.0888*cimentaciones_est - 0.0955*mesones_est - 0.2974*equipose_est + 0.0374*jardineria_est \
                   - 0.1470*senalizacion_est - 0.1760*urbanismo_est - 0.1644*imprevisto_est + 0.1104*honorarios_est

    preciom2 = (preciom2_est * diccionario['PrecioM2']['std'])+diccionario['PrecioM2']['mean']

    return math.ceil(preciom2)


@app.callback(
    Output(component_id='output1', component_property='children'),
    [
        Input(component_id='output', component_property='children'),
        Input(component_id='areaTotal', component_property='value'),
    ]
)

def total(output, areaTotal):
    return math.ceil(output*areaTotal)


if __name__ == '__main__':
    app.run_server()

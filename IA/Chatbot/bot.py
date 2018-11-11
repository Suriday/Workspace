#pip install ChatterBot
#Se necesita instalar mongodb
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 

chatbot = ChatBot(
    "Asistente Virtual",

    storage_adapter = 'chatterbot.storage.MongoDatabaseAdapter',
    database_uri = 'mongodb://localhost:27017/',
    database='chatterbot_asistente',

    input_adapter = "chatterbot.input.TerminalAdapter",
    output_adapter = "chatterbot.output.OutputAdapter",
    output_format="text",

    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'Disculpa, estoy aprendiendo a entenderte. ¿Puedes ser mas especifico?'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Desarrollador',
            'output_text': 'Ok, Facebook: https://www.facebook.com/pdts31'
        }
    ],

   preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ], 
    #Autoentrenamiento
    read_only=False,
)
#DEFAULT_SESSION_ID =chatbot.default_session.id

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("./train.yml")

while True:
    input_statement = chatbot.input.process_input_statement()
    statement, response = chatbot.generate_response(input_statement, 1)
    print("\n%s\n\n"%response)
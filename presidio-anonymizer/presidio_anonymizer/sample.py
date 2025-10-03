from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, entity_type: str, score: float, start: int, end: int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text, # input("text: "),
        analyzer_results=[RecognizerResult(entity_type, start, end, score)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    print(result)
    return result

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

if __name__ == "__main__": 
    returnedResult = sample_run_anonymizer("My name is Bond.", "PERSON", 0.8, 11, 15);

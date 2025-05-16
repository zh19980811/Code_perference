import random
import re

import datasets



def doc_to_text(doc: dict) -> str:
    return doc["input_final_prompts"][0]
def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc: dict) -> dict:
        out_doc = {
            "problem": doc["input_question"],
            "gold": doc["input_correct_responses"][0],
        }
        return out_doc
    dataset = dataset.select_columns(["input_question", "input_correct_responses", "input_final_prompts", "is_correct","input_question_hash","input_choice_list","output_prediction_text"])
    dataset = dataset.rename_column("is_correct","previously_is_correct")
    dataset = dataset.map(_process_doc)
    return dataset.map(_process_doc)

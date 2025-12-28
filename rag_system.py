# ============================================================
# rag_system.py — Standalone Offline Agricultural RAG Module
# ============================================================

import json

class OfflineAgriculturalRAG:

    def __init__(self, knowledge: dict):
        """
        RAG system backed by a structured dictionary.
        No embedding model required.
        """
        self.kb = knowledge
        print("RAG loaded successfully.")

    # ----------------------------------------------------------
    # Retrieve disease block from dictionary
    # ----------------------------------------------------------
    def get_disease_block(self, cnn_class_name, class_to_title):
        """
        Uses CNN class → human-readable title → disease dictionary block.
        """
        title = class_to_title.get(cnn_class_name)
        if not title:
            return {}

        block = self.kb["Diseases"].get(title, {})
        block = dict(block)
        block["name"] = title
        return block

    # ----------------------------------------------------------
    # STRICT extraction: Never hallucinate, only return existing fields
    # ----------------------------------------------------------
    def strict_extract(self, block):
        """
        Extracts only verified dictionary fields.
        If a field is not present in the knowledge, returns
        'Not specified in knowledge'.
        """
        fields = [
            "Confirmed Disease", "Symptoms", "Cause", "Organic Control",
            "Chemical Control", "Fertilizer Recommendation",
            "Climate Conditions", "Confusion With", "Prevention",
            "Dosage Information"
        ]

        output = {}

        for f in fields:

            if f == "Confirmed Disease":
                output[f] = block.get("name", "Not specified in knowledge")

            elif f == "Dosage Information":
                output[f] = self.kb.get("Dosages", {})

            else:
                output[f] = block.get(f, "Not specified in knowledge")

        return output

    # ----------------------------------------------------------
    # Natural response generator for chatbot / text interface
    # ----------------------------------------------------------
    def natural_text(self, extracted):
        """
        Makes a condensed human-readable explanation.
        """
        sections = []
        def add(name):
            if extracted[name] != "Not specified in knowledge":
                sections.append(f"{name}: {extracted[name]}")

        add("Confirmed Disease")
        add("Symptoms")
        add("Cause")
        add("Organic Control")
        add("Chemical Control")
        add("Prevention")
        add("Fertilizer Recommendation")
        return "\n".join(sections)

    # ----------------------------------------------------------
    # MASTER QUERY — takes user question + CNN prediction
    # ----------------------------------------------------------
    def query(self, user_question, prediction, class_to_title, ask_llm=False, llm_func=None):
        """
        Combines dictionary lookup + optional LLM summary.

        prediction = {"disease": "...", "confidence": float}
        """
        block = self.get_disease_block(prediction["disease"], class_to_title)
        extracted = self.strict_extract(block)
        natural = self.natural_text(extracted)

        response = {
            "extraction": extracted,
            "natural": natural
        }

        # ------------------------------------------------------
        # Optional LLM layer (Grounded — NO hallucination)
        # ------------------------------------------------------
        if ask_llm and llm_func is not None:
            prompt = f"""
You are an agricultural assistant. You MUST answer ONLY using this dictionary:

<<< KNOWLEDGE BLOCK >>>
{json.dumps(block, indent=2)}
<<< END >>>

User question:
{user_question}

Rules:
- No hallucination.
- If fertilizer is not available, say:
  "Fertilizer is not specified for this disease."
- Only use content present in the dictionary block.
"""

            response["llm_answer"] = llm_func(prompt)

        return response

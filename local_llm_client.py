def generate_with_optional_local_llm(prompt: str) -> tuple[bool, str, str]:
    """
    Attempts to generate an answer using a real local LLM backend (Ollama or Microsoft Foundry Local).
    Returns (True, answer, backend_name) if successful, or (False, error_message, "fallback") otherwise.
    """
    # 1. Check for Microsoft Foundry Local
    try:
        # Attempt to import Microsoft Foundry Local package
        import microsoft_foundry_local
        # Placeholder for real Foundry Local invocation:
        # client = microsoft_foundry_local.ChatClient()
        # response = client.complete(prompt)
        # return True, response, "Microsoft Foundry Local"
    except ImportError:
        pass
    except Exception as e:
        return False, f"Foundry Local error: {str(e)}", "fallback"

    # 2. Check for Ollama
    try:
        import ollama
        # Try to contact the local Ollama daemon and get model list
        model_list = ollama.list()
        models = model_list.get("models", [])
        if models:
            # Use the first available model in the list
            model_name = models[0]["name"]
            response = ollama.generate(model=model_name, prompt=prompt)
            answer = response.get("response", "").strip()
            if answer:
                return True, answer, f"Ollama ({model_name})"
    except ImportError:
        pass
    except Exception as e:
        # Ollama import succeeded but connection or runtime failed
        return False, f"Ollama runtime error: {str(e)}", "fallback"

    return False, "No active local LLM backend detected (Ollama / Foundry Local).", "fallback"

class ChatbotSINTA:
    def __init__(self):
        self.base_conhecimento = {
            "nivel_1": {
                "pergunta": "Em qual dia do início dos sintomas?",
                "opcoes": ["Menos de 7 dias", "7 dias ou mais"],
                "respostas": {
                    "Menos de 7 dias": "nivel_2",
                    "7 dias ou mais": "Chikungunya"
                }
            },
            "nivel_2": {
                "pergunta": "Teve febre alta? (38ºC ou mais)",
                "opcoes": ["Sim", "Não"],
                "respostas": {
                    "Sim": "nivel_3",
                    "Não": "Zika"
                }
            },
            "nivel_3": {
                "pergunta": "Teve manchas pelo corpo? (Sim/Não)",
                "opcoes": ["Sim", "Não"],
                "respostas": {
                    "Sim": "nivel_4",
                    "Não": "nivel_7"
                }
            },
            "nivel_4": {
                "pergunta": "Em qual dia do início dos sintomas as manchas apareceram?",
                "opcoes": ["Menos de 4 dias", "4 dias ou mais"],
                "respostas": {
                    "Menos de 4 dias": "nivel_9",
                    "4 dias ou mais": "nivel_5"
                }
            },
            "nivel_5": {
                "pergunta": "Houve dor e inchaço nas articulações? (Sim/Não)",
                "opcoes": ["Sim", "Não"],
                "respostas": {
                    "Sim": "Chikungunya",
                    "Não": "nivel_6"
                }
            },
            "nivel_6": {
                "pergunta": "Houve dor atrás dos olhos? (Sim/Não)",
                "opcoes": ["Sim", "Não"],
                "respostas": {
                    "Sim": "Dengue",
                    "Não": "nivel_7"
                }
            },
            "nivel_7": {
                "pergunta": "Teve náusea? (Sim/Não)",
                "opcoes": ["Sim", "Não"],
                "respostas": {
                    "Sim": "Dengue",
                    "Não": "Chikungunya"
                }
            },
            "nivel_8": {
                "pergunta": "Qual nível da coceira sentida? (Leve/Intensa/Moderada)",
                "opcoes": ["Leve", "Intensa/Moderada"],
                "respostas": {
                    "Leve": "nivel_7",
                    "Intensa/Moderada": "Zika"
                }
            },
            "nivel_9": {
                "pergunta": "Apresenta dor muscular?)",
                "opcoes": ["Sim", "Não"],
                "respostas": {
                    "Sim": "Chikungunya",
                    "Não": "Zika"
                }
            },
            "nivel_Extra": {
                "Zika": "Houve dor muscular? (Sim/Não)",
                "Dengue": "Qualquer resposta",
                "Chikungunya": "Houve dor muscular? (Sim/Não)"
            }
        }

        self.patient_profile = {}

    def iniciar_diagnostico(self):
        print("Bem-vindo ao Sistema de Diagnóstico SINTA!\n")
        self.diagnostico()

    def diagnostico(self):
        nivel_atual = "nivel_1"

        while True:
            pergunta_atual = self.base_conhecimento[nivel_atual]["pergunta"]
            opcoes = self.base_conhecimento[nivel_atual]["opcoes"]

            print(f"{pergunta_atual}")
            for i, opcao in enumerate(opcoes, start=1):
                print(f"{i}. {opcao}")

            escolha = input("Escolha a opção (1/2): ")
            opcao_escolhida = opcoes[int(escolha) - 1]

            self.patient_profile[nivel_atual] = opcao_escolhida

            if nivel_atual == "nivel_extra":
                proximo_nivel = self.base_conhecimento[nivel_atual][self.patient_profile["diagnostico"]]
            else:
                proximo_nivel = self.base_conhecimento[nivel_atual]["respostas"][opcao_escolhida]

            if proximo_nivel.startswith("nivel_"):
                nivel_atual = proximo_nivel
            else:
                print("\nDiagnóstico:")
                print(f"Você está infectado com: {proximo_nivel}")
                break


# Instanciar e executar o ChatbotSINTA
sinta = ChatbotSINTA()
sinta.iniciar_diagnostico()
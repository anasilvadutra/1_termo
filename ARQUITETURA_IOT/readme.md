
## 📡 1. Dispositivos de Redes: Ativos e Passivos

A infraestrutura de comunicação em IoT depende da combinação de elementos que processam dados e elementos que apenas guiam os sinais físicos.

### Ativos de Rede
Dispositivos que manipulam, direcionam ou amplificam os dados na rede. Eles possuem inteligência eletrônica e processamento.
* **Roteador:** Direciona pacotes de dados entre redes diferentes (ex: da rede local IoT para a nuvem).
* **Switch:** Conecta múltiplos dispositivos dentro da mesma rede local (LAN), direcionando o tráfego pelo endereço MAC.
* **Access Point (AP):** Converte a rede cabeada em sinal sem fio (Wi-Fi), essencial para a conexão de sensores.

### Passivos de Rede
Componentes físicos que servem de meio de transporte para os sinais, sem alterar ou processar os dados.
* **Cabo de Rede (UTP/STP):** Meio físico para transmissão elétrica de dados.
* **Fibra Óptica:** Meio físico para transmissão de dados através de pulsos de luz em longas distâncias.
* **Patch Panel e Conectores (RJ-45):** Estruturas de organização, fixação e terminação dos cabos de rede.

---

## ☁️ 2. Internet e suas Derivações

A evolução da conectividade moldou arquiteturas específicas para o tráfego massivo de dados gerados por máquinas.

* **M2M (Machine-to-Machine):** Comunicação direta entre dois dispositivos isolados, frequentemente via redes celulares (3G/4G/5G), sem intervenção humana.
* **IoT (Internet of Things):** Ecossistema global onde dispositivos coletam dados, interagem com servidores em nuvem e geram automações complexas.

---

## 🛠️ 3. Desenvolvimento com ESP32

O ESP32 é um microcontrolador de baixo custo e alta performance amplamente utilizado em projetos de IoT devido aos seus módulos integrados de Wi-Fi e Bluetooth.

### Driver do ESP32 e Configuração do Ambiente
Para que o computador consiga se comunicar e enviar código para a placa ESP32, é necessária a instalação de drivers específicos de conversão USB-Serial:
* **Driver CP210x** ou **CH340:** Chips comuns na base das placas ESP32 que criam uma porta COM virtual no sistema operacional.

### Código Exemplo: Conexão Wi-Fi no ESP32 (Arduino IDE)
```cpp
#include <WiFi.h>

const char* ssid = "Nome_da_Rede";
const char* password = "Senha_da_Rede";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi Conectado com sucesso!");
}

void loop() {}
```

---

## 📨 4. Protocolo MQTT (Message Queuing Telemetry Transport)

O MQTT é o protocolo padrão ouro para IoT. Ele opera na camada de aplicação, é extremamente leve e foi desenhado para redes instáveis ou de baixa largura de banda.

### Modelo Publish/Subscribe (Publicação/Assinatura)
Diferente do modelo HTTP (Cliente/Servidor), os dispositivos no MQTT não conversam diretamente. Eles usam um intermediário chamado **Broker**.
### Conceitos-Chave:
* **Broker:** O servidor central que recebe as mensagens e as distribui (ex: Mosquitto, HiveMQ).
* **Tópico:** O caminho estruturado para categorizar as mensagens (ex: `fabrica/maquina1/status`).
* **QoS (Quality of Service):** Define o nível de garantia da entrega da mensagem (Nível 0, 1 ou 2).

---

## 📄 5. Relatório Técnico de Arquitetura IoT

Estrutura formal recomendada para os alunos documentarem o projeto prático de arquitetura de redes e IoT.

1. **Introdução e Escopo do Projeto**
   * Descrição do problema que o sistema IoT resolve.
2. **Arquitetura de Hardware e Conectividade**
   * Modelo do microcontrolador (ESP32) e sensores utilizados.
   * Diagrama dos ativos e passivos de rede envolvidos no fluxo.
3. **Modelagem de Protocolo e Dados**
   * Topologia das mensagens MQTT (lista de tópicos e payloads).
   * Configuração do Broker utilizado.
4. **Resultados e Conclusão**
   * Validação do consumo de banda, latência e estabilidade da conexão.
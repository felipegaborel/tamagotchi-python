# 🐶 Tamagotchi Python

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Sobre

Projeto em Python que simula um Tamagotchi virtual. O código foi refatorado para usar atributos canônicos em inglês (name, health, hunger, energy, happiness, level, xp) e mantém aliases em português para compatibilidade (nome, saude, fome, energia, felicidade, nivel, xp).

Esta versão inclui:
- CLI interativo (terminal)
- Timeout de inatividade (se o usuário não responder dentro do tempo configurado, o pet morre)
- Versão web mínima para testes (Flask)

---

## 🚀 Tecnologias

- Python 3.8+
- Flask (apenas para a versão web)
- Colorama (para CLI colorido)
- PyTest (para testes, quando houver)

---

## Estrutura do projeto

```text
.
├─ main.py             # Entrypoint CLI (usa src/)
├─ web_app.py          # Versão web mínima (Flask) para testes
├─ src/                # Código do jogo (módulos)
└─ requirements-web.txt# Dependências para rodar a versão web
```

---

## 📦 Preparação do ambiente (local)

Recomenda-se usar um ambiente virtual.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-web.txt
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-web.txt
```

Observação:
- `requirements-web.txt` contém Flask para rodar a versão web. O resto do projeto não depende de muitas bibliotecas externas. Se você quiser instalar todas as dependências do ambiente de desenvolvimento do repositório, use `requirements.txt` (se existir), mas ele pode conter pacotes de notebooks/IDE.

---

## ▶️ Executando a versão CLI (terminal)

Execute a partir da raiz do repositório:

```bash
python main.py
```

- A CLI mostra um menu interativo.
- Se ficar inativo por 60 segundos (padrão), o pet morre. O timeout pode ser ajustado no código (`src/ui/menu.py`) modificando o parâmetro `timeout` passado para `mostrar_menu()` / `get_choice()`.

---

## 🌐 Executando a versão Web (local)

1. Certifique-se de ter instalado as dependências do `requirements-web.txt` (Flask).
2. Execute:

```bash
python web_app.py
```

3. Abra o navegador em `http://127.0.0.1:5000`.

Observações técnicas:
- `web_app.py` coloca automaticamente `src/` em `sys.path` para que os imports dos módulos do jogo funcionem sem precisar instalar o pacote.
- A versão web é um protótipo de teste em memória (não persiste entre reinícios). Para produção, conecte `SaveManager` ou um banco de dados.

### Implantação remota (ex.: Heroku / serviços com Procfile)

- Use Gunicorn para produção:

```bash
pip install gunicorn
gunicorn -w 4 web_app:app -b 0.0.0.0:$PORT
```

- Heroku: crie um `Procfile` com:

```
web: gunicorn web_app:app
```

- Assegure-se de adicionar `requirements-web.txt` (renomeie para `requirements.txt` se necessário pelo provedor) e empurre o repositório.

Deploy automático para Render (configuração recomendada)

Opção A — Deploy via integração direta do Render (recomendado, mais simples)

1. Crie uma conta em https://render.com e conecte o seu repositório GitHub ao Render.
2. No painel do Render, clique em "New" → "Web Service" e selecione o repositório `felipegaborel/tamagotchi-python`.
3. Configure o serviço:
   - Branch: `main`
   - Build Command: (deixe vazio ou use `pip install -r requirements-web.txt`)
   - Start Command: `gunicorn -w 4 web_app:app`
   - Environment: escolha a instance/tamanho desejado (para testes, a free-tier ou a smallest instance é suficiente).
4. Salve e crie o serviço. O Render fará o build e criará uma URL pública do tipo `https://<your-service>.onrender.com`.
5. Acesse essa URL para ver a versão web.

Opção B — Deploy via GitHub Actions + Render API (alternativa que já está configurada no repositório)

1. Criar Service no Render (como em A) e copiar o Service ID.
2. Criar uma API key em Render (Account → API Keys).
3. No GitHub (Settings → Secrets → Actions) adicione:
   - RENDER_API_KEY
   - RENDER_SERVICE_ID
4. Fazer push para main; o workflow `.github/workflows/deploy-render.yml` será executado e acionará a API do Render para criar um novo deploy.

Observações importantes para Render (diretamente via painel)
- Certifique-se de ter `requirements-web.txt` com `gunicorn` e `Flask` (já incluso no repo). O Render detecta automaticamente um Procfile se presente; o repositório inclui `Procfile` com `web: gunicorn web_app:app`.
- Adicione variáveis de ambiente no painel do Render se precisar (por exemplo: configuração de DEBUG, chaves externas, etc.).
- O endpoint `/health` foi adicionado em `web_app.py` para healthchecks (Render usará sua própria checagem, mas um health endpoint simples é recomendado).

---

## 🧪 Testes e Lint

- Para rodar testes (se houver):

```bash
pytest -q
```

- Recomendado adicionar CI (GitHub Actions) com linters (ruff/flake8) e mypy. Posso criar um workflow de CI se desejar.

---

## 🔧 Observações de manutenção

- O código principal foi refatorado para usar atributos canônicos em inglês; métodos e nomes em português permanecem como aliases para compatibilidade.
- Arquivo `src/ui/menu.py` implementa entrada com timeout (cross-platform).
- `web_app.py` é um protótipo destinado a testes rápidos.

---

## 📬 Contribuições

Contribuições são bem-vindas! Abra issues ou PRs no GitHub.

## 👨‍💻 Autor

Felipe Gabriel Barbosa

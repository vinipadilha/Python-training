from market import app, db

if __name__ == "__main__":
    # Cria as tabelas (se não existirem) dentro do contexto da aplicação
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
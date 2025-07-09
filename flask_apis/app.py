from server import create_app,db


#create app instance
app = create_app()


if __name__ == "__main__":
    #add host as 0.0.0.0 to be accessible from outside when running as a #container
    #app.run(host='0.0.0.0')
    with app.app_context():
        write_engine = db.get_engine(bind='write')
        read_engine = db.get_engine(bind='read')
        with write_engine.connect() as conn:
            print("✅ Write DB connected:", conn.execute("SELECT 1").scalar())
        with read_engine.connect() as conn:
            print("✅ Read DB connected:", conn.execute("SELECT 1").scalar())
    app.run(debug=True, port=8000, host='0.0.0.0')
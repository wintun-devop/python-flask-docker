from server import create_app,db
#import blue print
from server.routes.server_test import api_test_bp
from server.routes.app.product import product_bp

#create app instance
app = create_app()

#register Blue print
app.register_blueprint(api_test_bp)
app.register_blueprint(product_bp)


if __name__ == "__main__":
    #add host as 0.0.0.0 to be accessible from outside when running as a #container
    #app.run(host='0.0.0.0')
    # with app.app_context():
    #     write_engine = db.get_engine(bind='write')
    #     read_engine = db.get_engine(bind='read')
    #     with write_engine.connect() as conn:
    #         print("✅ Write DB connected:", conn.execute("SELECT 1").scalar())
    #     with read_engine.connect() as conn:
    #         print("✅ Read DB connected:", conn.execute("SELECT 1").scalar())
    app.run(debug=True)
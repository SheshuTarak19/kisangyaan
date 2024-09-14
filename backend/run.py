from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    
    # Register routes
    from app.routes import main,voicesearch,onsubmit,growthtrack,waterstress,diseasedetection,environ,automated,crophealth,growthprediction,marketsales,supplychain,automatedtskmange
    app.register_blueprint(main)
    app.register_blueprint(voicesearch)
    app.register_blueprint(waterstress)
    app.register_blueprint(onsubmit)
    app.register_blueprint(growthtrack)
    app.register_blueprint(diseasedetection)
    app.register_blueprint(environ)
    app.register_blueprint(automated)
    app.register_blueprint(crophealth)
    app.register_blueprint(growthprediction)
    app.register_blueprint(marketsales)
    app.register_blueprint(supplychain)
    app.register_blueprint(automatedtskmange)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

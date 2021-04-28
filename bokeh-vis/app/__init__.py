from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from bokeh.models import ColumnDataSource
#from bokeh.plotting import figure, output_file, show

#Source = ColumnDataSource()

#fig = figure(plot_height=600, plot_width=720, tooltips=[("Tile", "@title"), ("Released", "@released")])
#fig.circle(x="x", y="y", source=source, size=8, color="color", line_color=None)
#fig.xaxis.axis_label

db = SQLAlchemy()

def create_app():
    # """ constructing the core app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes 

        db.create_all() # create tables for our data models

        return app

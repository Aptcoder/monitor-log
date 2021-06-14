from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == "warning":
      app.logger.warning("warning")
    elif log == "info":
      app.logger.info("info")
    elif log == "error":
      app.logger.error("error")
    elif log == "critical":
      app.logger.critical("critical")
      
    return render_template(
        'index.html',
        log=log
    )

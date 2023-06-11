import subprocess

from flask import Flask, make_response, render_template
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

@api.resource("/elf/<file>")
class ElfPayload(flask_restful.Resource):
    def get(self, file: str):
        script: str = ""
        cmd = f'fee "./elf/{file}"'
        try:
            p = subprocess.run(
                    cmd, shell=True,
                    capture_output=True,
                    timeout=60
                )
            if not p.stdout.startswith(b"import"):
                raise Exception("error generating payload")

            script = p.stdout
        except Exception as ex:
            # TODO: Make this 402 something appropriate and not just funny
            return {'error': f'error processing: {ex}'}, 402

        response = make_response(script, 200)
        response.mimetype = "text/plain"
        return response


@api.resource("/sc/<file>")
class ShellcodePayload(flask_restful.Resource):
    def get(self, file: str):
        script = ''
        try:
            with open(f'./shellcode/{file}', 'rb') as f:
                bs: bytes = f.read()
            script = render_template('sc.py', escaped_hex=bs) 
        except Exception as ex:
            # TODO: Make this 402 something appropriate and not just funny
            return {'error': f'error processing: {ex}'}, 402

        response = make_response(script, 200)
        response.mimetype = "text/plain"
        return response


@api.resource("/py/<file>")
class PythonPayload(flask_restful.Resource):
    def get(self, file: str):
        script = ''
        try:
            with open(f'./python/{file}', 'rb') as f:
                script = f.read()
        except Exception as ex:
            # TODO: Make this 402 something appropriate and not just funny
            return {'error': f'error processing: {ex}'}, 402

        response = make_response(script, 200)
        response.mimetype = "text/plain"
        return response


if __name__ == '__main__':
    app.run()

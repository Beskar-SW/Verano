const root_element = document.getElementById('root');

class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            emailError: false,
            verify: false,
        };
    }

    handleEmailChange = (e) => {
        this.setState({ email: e.target.value });
        if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(e.target.value)){
            this.setState({emailError: false});
        }else if(e.target.value.length == 0){
            this.setState({emailError: false});
        }
        else{
            this.setState({emailError: true});
            this.setState({emailErrorMessage: 'Correo inválido'});
        }
    };

    handlePasswordChange = (e) => {
        this.setState({ password: e.target.value });
    };

    render() {
        return (
            <div className="container">
                <form action="/profesores/login" method="post">

                    <img src={"/static/img/itz.png"} className="logo"></img>

                    <div className="form-group">
                        <label htmlFor="email">Correo:</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            name="email"
                            value={this.state.email}
                            onChange={this.handleEmailChange}
                            placeholder="Ingresa tu correo"
                        />
                        {this.state.emailError ? <small id="emailHelp" class="form-text text-danger">{this.state.emailErrorMessage}</small> : <small id="emailHelp" class="form-text text-muted">Nunca compartiremos tu correo con nadie más.</small>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Contraseña:</label>
                        <div style={{position:'relative'}}>
                            <input
                                type= {this.state.verify ? "text" : "password"}
                                className="form-control"
                                id="password"
                                name="password"
                                value={this.state.password}
                                onChange={this.handlePasswordChange}
                                placeholder="Ingresa tu contraseña"
                            />
                            {this.state.verify ? <i className="eye" onClick={() => {this.setState({verify: !this.state.verify})}}>🤔</i> : <i className="eye" onClick={() => {this.setState({verify: !this.state.verify})}}>🫣</i>}
                        </div>
                    </div>
                    <button type="submit" className="btn btn-primary">Iniciar sesión</button>
                </form>
            </div>
        );
    }
}

class App extends React.Component {
    constructor(props) {
        super(props);
    }


    render() {
        return (
            <div>
                <LoginForm />
            </div>
        );
    }
}

ReactDOM.render(<App />, root_element);

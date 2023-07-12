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

    handleSubmit = (e) => {
        e.preventDefault();
        fetch('/login',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: this.state.email,
                password: this.state.password
            })
        }).catch(err => console.log(err));
    };

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
                {/* <form onSubmit={this.handleSubmit}> */}
                <form action="/login" method="post">

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
                    {/* <button type="button " className="btn btn-primary" onClick={this.handleSubmit}>Iniciar sesión</button> */}
                    <button type="submit" className="btn btn-primary">Iniciar sesión</button>
                    <p>No tienes una cuenta? <a href="javascript:void(0);" onClick={() => this.props.y(true)}>Regístrate</a></p>

                </form>
            </div>
        );
    }
}
class RegisterForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fullName: '',
            studentNumber: '',
            email: '',
            password: '',
            confirmPassword: '',
            studentNumberError: false,
            emailError: false,
            passwordError: false,
            secondPasswordError: false,
            verify: false,
            studentNumberMessage: '',
            emailErrorMessage: '',
            passwordErrorMessage: '',
            confirmPasswordErrorMessage: ''
        };
    }

    handleFullNameChange = (e) => {
        this.setState({ fullName: e.target.value });
    };

    handleStudentNumberChange = (e) => {
        this.setState({ studentNumber: e.target.value });
        if(/^\d{8}$/.test(e.target.value)){
            this.setState({studentNumberMessage: 'Número de control valido'})
            this.setState({studentNumberError: false});
        }else if(e.target.value.length == 0){
            this.setState({studentNumberMessage: ''})
            this.setState({studentNumberError: true});
        }else{
            this.setState({studentNumberMessage: 'Número de control invalido'})
            this.setState({studentNumberError: true});
        }
    };

    handleEmailChange = (e) => {
        this.setState({ email: e.target.value });
        if(/^\w+([\.-]?\w+)*@itz.edu.mx$/.test(e.target.value)){
            this.setState({emailErrorMessage: 'Correo valido'})
            this.setState({emailError: false});
        }else if(e.target.value.length == 0){
            this.setState({emailErrorMessage: ''})
            this.setState({emailError: true});
        }else{
            this.setState({emailErrorMessage: 'Correo invalido'})
            this.setState({emailError: true});
        }
    };

    handlePasswordChange = (e) => {
        this.setState({ password: e.target.value });
        // Debe contener 1 letra mayúscula, 1 letra minúscula, 1 número, 1 caracter especial y tener una longitud de al menos 8 caracteres
        if(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,}$/.test(e.target.value)){
            this.setState({passwordErrorMessage: 'Contraseña valida'})
            this.setState({passwordError: false});
        }else if(e.target.value.length == 0){
            this.setState({passwordErrorMessage: ''})
            this.setState({passwordError: true});
        }else{
            this.setState({passwordErrorMessage: 'Contraseña invalida'})
            this.setState({passwordError: true});
        }
    };

    handleConfirmPasswordChange = (e) => {
        this.setState({ confirmPassword: e.target.value });
        if(e.target.value == this.state.password){
            this.setState({secondPasswordError: false});
            this.setState({confirmPasswordErrorMessage: 'Contraseña valida'})
        }else if(e.target.value.length == 0){
            this.setState({secondPasswordError: true});
            this.setState({confirmPasswordErrorMessage: ''})
        }
        else{
            this.setState({secondPasswordError: true});
            this.setState({confirmPasswordErrorMessage: 'Las contraseñas no coinciden'})
        }
    };

    render() {
        return (
            <div className="container">
                <form action="/registro" method="post">
                    <div className="form-group">
                        <label htmlFor="fullName" className="form-label">Nombre completo:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="fullName"
                            name="fullName"
                            value={this.state.fullName}
                            onChange={this.handleFullNameChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="studentNumber" className="form-label">Número de control:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="studentNumber"
                            name="studentNumber"
                            value={this.state.studentNumber}
                            onChange={this.handleStudentNumberChange}
                        />
                        {this.state.studentNumberError ? <small id="studentNumberHelp" class="form-text text-danger">{this.state.studentNumberMessage}</small> : <small id="studentNumberHelp" class="form-text text-success">{this.state.studentNumberMessage}</small>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="email" className="form-label">Correo institucional:</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            name="email"
                            value={this.state.email}
                            onChange={this.handleEmailChange}
                        />
                        {this.state.emailError ? <small id="emailHelp" class="form-text text-danger">{this.state.emailErrorMessage}</small> : <small id="emailHelp" class="form-text text-success">{this.state.emailErrorMessage}</small>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="password" className="form-label">Contraseña:</label>
                        <div style={{position:'relative'}}>
                            <input
                                type={this.state.verify ? "text" : "password"}
                                className="form-control"
                                id="password"
                                name="password"
                                value={this.state.password}
                                onChange={this.handlePasswordChange}
                            />
                            {this.state.verify ? <i className="eye" onClick={() => {this.setState({verify: !this.state.verify})}}>🤔</i> : <i className="eye" onClick={() => {this.setState({verify: !this.state.verify})}}>🫣</i>}
                        </div>
                        {this.state.passwordError ? <small id="passwordHelp" class="form-text text-danger">{this.state.passwordErrorMessage}</small> : <small id="passwordHelp" class="form-text text-success">{this.state.passwordErrorMessage}</small>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="confirmPassword" className="form-label">Confirmar contraseña:</label>
                        <input
                            type="password"
                            className="form-control"
                            id="confirmPassword"
                            name="confirmPassword"
                            value={this.state.confirmPassword}
                            onChange={this.handleConfirmPasswordChange}
                        />
                        {this.state.secondPasswordError ? <small id="confirmPasswordHelp" class="form-text text-danger">{this.state.confirmPasswordErrorMessage}</small> : <small id="confirmPasswordHelp" class="form-text text-success">{this.state.confirmPasswordErrorMessage}</small>}
                    </div>
                    <button type="submit" className="btn btn-primary">Registrarse</button>
                    <p>Ya tienes una cuenta? <a href="javascript:void(0);" onClick={() => this.props.y(false)}>Inicia sesión</a></p>
                </form>
            </div>
        );
    }
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            haveAccount: data.toLowerCase() == 'true' ? true : false,
        };
    }

    handleClick = () => {
        this.setState({ haveAccount: !this.state.haveAccount });
    };

    render() {
        return (
            <div>
                {this.state.haveAccount ? <LoginForm y={this.handleClick} /> : <RegisterForm y={this.handleClick} />}
            </div>
        );
    }
}

ReactDOM.render(<App />, root_element);

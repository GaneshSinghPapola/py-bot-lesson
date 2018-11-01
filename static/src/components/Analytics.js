import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom'
import PropTypes from 'prop-types';
import * as actionCreators from '../actions/auth';
import Pusher from 'pusher-js';
import './css/chatBox.css'
import './css/chatList.css'
import {API_URL, URL} from '../constants';

function mapStateToProps(state) {
    return {
        isRegistering: state.auth.isRegistering,
        registerStatusText: state.auth.registerStatusText,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}




class Analytics extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          text: '',
          username: '',
          chats: []
        };
      }
    componentDidMount(){
        const pusher = new Pusher('5982c2cccbde01cd2bac', {
            cluster: 'ap2',
            encrypted: true
          });
          const channel = pusher.subscribe('chat');
          channel.bind('message', data => {
            this.setState({ chats: [...this.state.chats, data], test: '' });
          });   
    }


    async handleTextChange(e) {
        let text = e.target.value; 
        if (e.keyCode === 13) {
          const payload = {
            username: this.state.username,
            message: this.state.text
          };
          const res = await fetch(`${API_URL}/dialog`,{method:"POST",headers:
          {"Content-Type":"application/json",'Access-Control-Allow-Origin':'*'},body:payload}) 
          console.log('res from server is >> ',res)
        } else {
          this.setState({ text });
        }
      }

    render() {
        return (
            <div className="col-md-8">
                <h1>Help</h1>
                <hr />
                <section>
                <ul>
                    {this.state.chats.map(chat => {
                    return (
                        <div>
                            <div className="row show-grid">
                                <div className="col-xs-12">
                                    <div className="chatMessage">
                                        <div key={chat.id} className="box">
                                            <p>
                                                <strong>{chat.username}</strong>
                                            </p>
                                            <p>{chat.message}</p>
                                        </div>
                                        <div className="imageHolder">
                                            {/* <img src={avatar} className="img-responsive avatar" alt="logo" /> */}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    );
                    })}
  </ul>

    <div>
        <div className="row">
                <div className="col-md-8">
                    <div className="chat">
                        <div className="col-md-8">
                            <input
                                type="text"
                                value={this.state.text}
                                placeholder="chat here..."
                                className="form-control"
                                onChange={(e)=>this.handleTextChange(e)}
                                onKeyDown={(e)=>this.handleTextChange(e)}
                            />
                        </div>

                        <div className="clearfix"></div>
                    </div>
                </div>
                <h4 className="greetings">Hello, {this.state.username}</h4>
            </div>
        </div>

                </section>
            </div>
        );
    }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Analytics));
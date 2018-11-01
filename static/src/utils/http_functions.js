/* eslint camelcase: 0 */

import axios from 'axios';

const tokenConfig = (token) => ({
    headers: {
        'Authorization': token, // eslint-disable-line quote-props
    },
});

export function validate_token(token) {
    return axios.post('/api/v1/is_token_valid', {
        token,
    });
}

export function get_github_access() {
    window.open(
        '/github-login',
        '_blank' // <- This is what makes it open in a new window.
    );
}

export function create_user(props) {
    const keys = Object.keys(props)
    let formdata = new FormData();

        for (const key of keys) {
                console.log(key)
                console.log("=-=-=-=-=-=-=-=-=-=-\n\n",props[key])
                if(key === 'image')
                formdata.append(key,props[key]) 
                else
                formdata.append(key, props[key])
                console.log(formdata)
        }
    return axios.post('api/v1/create_user',
        formdata,
        {
            headers: { 'Accept': 'application/json','Content-Type': 'multipart/form-data' }
    });
}

export function get_token(email, password) {
    return axios.post('api/v1/get_token', {
        email,
        password,
    });
}

export function has_github_token(token) {
    return axios.get('api/v1/has_github_token', tokenConfig(token));
}

export function data_about_user(token) {
    return axios.get('api/v1/user', tokenConfig(token));
}

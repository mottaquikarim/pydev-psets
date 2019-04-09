import React, {
    createContext,
    useReducer,
} from 'react';

const initialState = {
    files: {},
    currentFile: {},
}
const reducer = (state, action) => {
    switch (action.type) {
        case "UPDATE_FILES":
            return {...state, files: action.payload};
        case "UPDATE_CURRENT_FILE":
            return {...state, currentFile: action.payload};
        case "UPDATE_CURRENT_FILE_CONTENT":
            return {...state, currentFile: action.payload};
        case "UPDATE_LOADING":
            return {...state, loading: action.payload};
        default:
            return {...state};
    }
}
const StateContext = createContext(initialState);
const StateProvider = props => {
    const [state, dispatch] = useReducer(reducer, initialState);
    return <StateContext.Provider value={{state, dispatch}}>
        {props.children}
    </StateContext.Provider>
}

export {StateContext, StateProvider}

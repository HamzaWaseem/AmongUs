import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import CloudSecurity from './pages/CloudSecurity';
import Compliance from './pages/Compliance';
import DataEncryption from './pages/DataEncryption';
import DependencyManagement from './pages/DependencyManagement';

const theme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: '#2196f3',
        },
        secondary: {
            main: '#f50057',
        },
    },
});

function App() {
    return ( <
        ThemeProvider theme = { theme } >
        <
        CssBaseline / >
        <
        Router >
        <
        Layout >
        <
        Routes >
        <
        Route path = "/"
        element = { < Dashboard / > }
        /> <
        Route path = "/cloud-security"
        element = { < CloudSecurity / > }
        /> <
        Route path = "/compliance"
        element = { < Compliance / > }
        /> <
        Route path = "/data-encryption"
        element = { < DataEncryption / > }
        /> <
        Route path = "/dependency-management"
        element = { < DependencyManagement / > }
        /> < /
        Routes > <
        /Layout> < /
        Router > <
        /ThemeProvider>
    );
}

export default App;
import React, { useState } from 'react';
import {
    Box,
    Card,
    CardContent,
    Typography,
    Grid,
    TextField,
    Button,
    Alert,
    List,
    ListItem,
    ListItemText,
    ListItemIcon,
    Chip,
} from '@mui/material';
import {
    CheckCircle as CheckIcon,
    Error as ErrorIcon,
    Pending as PendingIcon,
} from '@mui/icons-material';
import axios from 'axios';

function DependencyManagement() {
    const [packageInfo, setPackageInfo] = useState({
        name: '',
        version: '',
    });
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);

    const handleInputChange = (e) => {
        setPackageInfo({
            ...packageInfo,
            [e.target.name]: e.target.value,
        });
    };

    const handleCheckPackage = async(e) => {
        e.preventDefault();
        setError(null);
        try {
            const response = await axios.post('/api/dependencies/check-package', packageInfo);
            setResults(response.data);
        } catch (err) {
            setError(err.response ? .data ? .error || 'An error occurred');
        }
    };

    const handleScanRequirements = async() => {
        setError(null);
        try {
            const response = await axios.post('/api/dependencies/scan-requirements');
            setResults(response.data.results);
        } catch (err) {
            setError(err.response ? .data ? .error || 'An error occurred');
        }
    };

    const getStatusIcon = (status) => {
        switch (status) {
            case 'secure':
                return <CheckIcon color = "success" / > ;
            case 'vulnerable':
                return <ErrorIcon color = "error" / > ;
            default:
                return <PendingIcon color = "warning" / > ;
        }
    };

    return ( <
        Box >
        <
        Typography variant = "h4"
        gutterBottom >
        Dependency Management <
        /Typography>

        <
        Grid container spacing = { 3 } >
        <
        Grid item xs = { 12 }
        md = { 6 } >
        <
        Card >
        <
        CardContent >
        <
        Typography variant = "h6"
        gutterBottom >
        Check Package Security <
        /Typography> <
        form onSubmit = { handleCheckPackage } >
        <
        TextField fullWidth label = "Package Name"
        name = "name"
        value = { packageInfo.name }
        onChange = { handleInputChange }
        margin = "normal"
        required helperText = "Enter package name (e.g., react)" /
        >
        <
        TextField fullWidth label = "Version"
        name = "version"
        value = { packageInfo.version }
        onChange = { handleInputChange }
        margin = "normal"
        helperText = "Leave empty for latest version" /
        >
        <
        Button type = "submit"
        variant = "contained"
        color = "primary"
        sx = {
            { mt: 2, mr: 2 }
        } >
        Check Package <
        /Button> <
        Button variant = "outlined"
        color = "primary"
        onClick = { handleScanRequirements }
        sx = {
            { mt: 2 }
        } >
        Scan requirements.txt <
        /Button> < /
        form > <
        /CardContent> < /
        Card > <
        /Grid>

        <
        Grid item xs = { 12 }
        md = { 6 } > {
            error && ( <
                Alert severity = "error"
                sx = {
                    { mb: 2 }
                } > { error } <
                /Alert>
            )
        } {
            results && ( <
                Card >
                <
                CardContent >
                <
                Typography variant = "h6"
                gutterBottom >
                Security Scan Results <
                /Typography> <
                List > {
                    Array.isArray(results) ? (
                        results.map((result, index) => ( <
                            ListItem key = { index } >
                            <
                            ListItemIcon > { getStatusIcon(result.status) } <
                            /ListItemIcon> <
                            ListItemText primary = { result.name }
                            secondary = { `Version: ${result.current_version || 'N/A'}` }
                            /> <
                            Chip label = { result.status }
                            color = {
                                result.status === 'secure' ?
                                'success' : result.status === 'vulnerable' ?
                                    'error' : 'warning'
                            }
                            size = "small" /
                            >
                            <
                            /ListItem>
                        ))
                    ) : ( <
                        ListItem >
                        <
                        ListItemIcon > { getStatusIcon(results.status) } < /ListItemIcon> <
                        ListItemText primary = { results.name }
                        secondary = { <
                            pre style = {
                                { whiteSpace: 'pre-wrap' }
                            } > { JSON.stringify(results, null, 2) } <
                            /pre>
                        }
                        /> < /
                        ListItem >
                    )
                } <
                /List> < /
                CardContent > <
                /Card>
            )
        } <
        /Grid> < /
        Grid > <
        /Box>
    );
}

export default DependencyManagement;
import React, { useState } from 'react';
import {
    Box,
    Card,
    CardContent,
    Typography,
    TextField,
    Button,
    Grid,
    Alert,
} from '@mui/material';
import axios from 'axios';

function CloudSecurity() {
    const [awsCredentials, setAwsCredentials] = useState({
        accessKey: '',
        secretKey: '',
        region: 'us-east-1',
    });
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);

    const handleInputChange = (e) => {
        setAwsCredentials({
            ...awsCredentials,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            const response = await axios.post('/api/cloud-security/check-aws', awsCredentials);
            setResults(response.data);
        } catch (err) {
            setError(err.response?.data?.error || 'An error occurred');
        }
        try {
            const response = await axios.get('/api/cloud-security/scan');
            setResults(response.data);
        } catch (err) {
            setError(err.response?.data?.error || 'An error occurred');
        }
    };

    return ( <
        Box >
        <
        Typography variant = "h4"
        gutterBottom >
        Cloud Security Audit <
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
        AWS Security Check <
        /Typography> <
        form onSubmit = { handleSubmit } >
        <
        TextField fullWidth label = "AWS Access Key"
        name = "accessKey"
        value = { awsCredentials.accessKey }
        onChange = { handleInputChange }
        margin = "normal"
        required /
        >
        <
        TextField fullWidth label = "AWS Secret Key"
        name = "secretKey"
        type = "password"
        value = { awsCredentials.secretKey }
        onChange = { handleInputChange }
        margin = "normal"
        required /
        >
        <
        TextField fullWidth label = "AWS Region"
        name = "region"
        value = { awsCredentials.region }
        onChange = { handleInputChange }
        margin = "normal" /
        >
        <
        Button type = "submit"
        variant = "contained"
        color = "primary"
        sx = {
            { mt: 2 }
        } >
        Run Security Check <
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
                Results <
                /Typography> <
                pre style = {
                    { whiteSpace: 'pre-wrap' }
                } > { JSON.stringify(results, null, 2) } <
                /pre> < /
                CardContent > <
                /Card>
            )
        } <
        /Grid> < /
        Grid > <
        /Box>
    );
}

export default CloudSecurity;
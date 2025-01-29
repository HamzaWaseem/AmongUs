import React, { useState } from 'react';
import {
    Box,
    Card,
    CardContent,
    Typography,
    Grid,
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

const complianceFrameworks = [
    { id: 'gdpr', name: 'GDPR', description: 'General Data Protection Regulation' },
    { id: 'hipaa', name: 'HIPAA', description: 'Health Insurance Portability and Accountability Act' },
    { id: 'pci', name: 'PCI DSS', description: 'Payment Card Industry Data Security Standard' },
    { id: 'sox', name: 'SOX', description: 'Sarbanes-Oxley Act' },
];

function Compliance() {
    const [selectedFramework, setSelectedFramework] = useState(null);
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);

    const handleCheckCompliance = async(framework) => {
        setError(null);
        setSelectedFramework(framework);
        try {
            const response = await axios.get(`/api/compliance/check-${framework}`);
            setResults(response.data);
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
        Compliance Audit <
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
        Select Compliance Framework <
        /Typography> <
        List > {
            complianceFrameworks.map((framework) => ( <
                ListItem key = { framework.id }
                secondaryAction = { <
                    Button
                    variant = "contained"
                    onClick = {
                        () => handleCheckCompliance(framework.id)
                    } >
                    Check Compliance <
                    /Button>
                } >
                <
                ListItemText primary = { framework.name }
                secondary = { framework.description }
                /> < /
                ListItem >
            ))
        } <
        /List> < /
        CardContent > <
        /Card> < /
        Grid >

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
                gutterBottom > { selectedFramework ? .toUpperCase() }
                Compliance Results <
                /Typography> <
                List > {
                    results.checks ? .map((check, index) => ( <
                        ListItem key = { index } >
                        <
                        ListItemIcon > { getStatusIcon(check.status) } < /ListItemIcon> <
                        ListItemText primary = { check.name }
                        secondary = { check.details }
                        /> <
                        Chip label = { check.status }
                        color = {
                            check.status === 'secure' ?
                            'success' : check.status === 'vulnerable' ?
                                'error' : 'warning'
                        }
                        size = "small" /
                        >
                        <
                        /ListItem>
                    ))
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

export default Compliance;
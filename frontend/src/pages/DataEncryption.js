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

function DataEncryption() {
    const [tlsCheck, setTlsCheck] = useState({
        hostname: '',
        port: '443',
    });
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);

    const handleInputChange = (e) => {
        setTlsCheck({
            ...tlsCheck,
            [e.target.name]: e.target.value,
        });
    };

    const handleCheckTLS = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            // Fixed the API endpoint to match Django's URL configuration
            const response = await axios.post('http://localhost:8000/service_https_certificate/check-tls/', tlsCheck);
            setResults(response.data);
        } catch (err) {
            setError(err.response?.data?.error || 'An error occurred');
        }
    };

    const getStatusIcon = (status) => {
        switch (status) {
            case 'secure':
                return <CheckIcon color="success" />;
            case 'vulnerable':
                return <ErrorIcon color="error" />;
            default:
                return <PendingIcon color="warning" />;
        }
    };

    return (
        <Box>
            <Typography variant="h4" gutterBottom>
                Data Encryption Audit
            </Typography>

            <Grid container spacing={3}>
                <Grid item xs={12} md={6}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6" gutterBottom>
                                TLS/SSL Configuration Check
                            </Typography>
                            <form onSubmit={handleCheckTLS}>
                                <TextField
                                    fullWidth
                                    label="Hostname"
                                    name="hostname"
                                    value={tlsCheck.hostname}
                                    onChange={handleInputChange}
                                    margin="normal"
                                    required
                                    helperText="Enter domain name (e.g., example.com)"
                                />
                                <TextField
                                    fullWidth
                                    label="Port"
                                    name="port"
                                    type="number"
                                    value={tlsCheck.port}
                                    onChange={handleInputChange}
                                    margin="normal"
                                    helperText="Default: 443"
                                />
                                <Button
                                    type="submit"
                                    variant="contained"
                                    color="primary"
                                    sx={{ mt: 2 }}
                                >
                                    Check TLS Configuration
                                </Button>
                            </form>
                        </CardContent>
                    </Card>
                </Grid>

                <Grid item xs={12} md={6}>
                    {error && (
                        <Alert severity="error" sx={{ mb: 2 }}>
                            {error}
                        </Alert>
                    )}
                    {results && (
                        <Card>
                            <CardContent>
                                <Typography variant="h6" gutterBottom>
                                    TLS Configuration Results
                                </Typography>
                                <List>
                                    <ListItem>
                                        <ListItemIcon>{getStatusIcon(results.status)}</ListItemIcon>
                                        <ListItemText
                                            primary="Overall Status"
                                            secondary={results.status}
                                        />
                                    </ListItem>
                                    {results.details && (
                                        <>
                                            <ListItem>
                                                <ListItemText
                                                    primary="Protocol Version"
                                                    secondary={results.details.protocol_version}
                                                />
                                            </ListItem>
                                            <ListItem>
                                                <ListItemText
                                                    primary="Cipher Suite"
                                                    secondary={results.details.cipher_suite}
                                                />
                                            </ListItem>
                                            <ListItem>
                                                <ListItemText
                                                    primary="Certificate Details"
                                                    secondary={
                                                        <pre style={{ whiteSpace: 'pre-wrap' }}>
                                                            {JSON.stringify(results.details.certificate, null, 2)}
                                                        </pre>
                                                    }
                                                />
                                            </ListItem>
                                        </>
                                    )}
                                </List>
                            </CardContent>
                        </Card>
                    )}
                </Grid>
            </Grid>
        </Box>
    );
}

export default DataEncryption;
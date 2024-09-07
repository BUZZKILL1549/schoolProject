try {
    # Execute the MySQL command and capture both standard output and errors
    $output = Get-Content initializeDatabase.sql | mysql -u root -p school_app 2>&1

    # Check the last exit code; if it's not 0, an error occurred
    if ($LASTEXITCODE -ne 0) {
        # Look for specific error messages in the output
        if ($output -match "ERROR 1007") {
            Write-Output "Database already exists."
        } elseif ($output -match "ERROR 1050") {
            Write-Output "Table already exists."
        } else {
            Write-Output "An unexpected error occured: $output"
        }
    } else {
        # If there were no errors, indicate success
        Write-Output "Database initialized successfully."
    }
}
catch {
    # Catch any unforeseen errors and print a generic message
    Write-Output "Failed to execute MySQL command: $_"
}

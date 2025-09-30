- I noticed that some of the projects are using serverless architecture. Previous devops engineer created a serverless yml file for one among the service, and team followed the skeleton of the serverless architecture. During development some developers missed purne (serverless-prune-plugin) due to this the new versions are getting created and older versions are remain same because of this the cost for the lambda service is increase as the code limit is 75GB it reached and further extended to 300GB. I noticed and informed the manager and take temparary and permananent step
- Temparary steps
- created aws secret key and id using iam role and followed the steps
### set desired account 
```sh
aws configure
aws lambda list-functions --query 'Functions[*].FunctionName' --output table
```
### available versions
```sh
$functions = aws lambda list-functions --query 'Functions[*].FunctionName' --output text
foreach ($fn in $functions.Split("`t")) {
    Write-Host "=== Versions for $fn ==="
    aws lambda list-versions-by-function --function-name $fn --query 'Versions[*].[Version,CodeSize,LastModified]' --output table
}
```

### Dry run
```sh
$functions = aws lambda list-functions --query 'Functions[*].FunctionName' --output text

foreach ($fn in $functions.Split("`t")) {
    Write-Host "=== Checking versions for $fn ==="

    # Get versions sorted by LastModified (exclude $LATEST)
    $versions = aws lambda list-versions-by-function --function-name $fn `
        --query 'Versions[?Version!=`$LATEST`].[Version,LastModified]' `
        --output json | ConvertFrom-Json | Sort-Object { $_[1] } -Descending

    if ($versions.Count -gt 4) {
        # Identify versions to delete but do not delete them
        $toDelete = $versions | Select-Object -Skip 4

        foreach ($ver in $toDelete) {
            $verNum = $ver[0]
            Write-Host "Would delete version $verNum of $fn"
        }
    } else {
        Write-Host "No cleanup needed for $fn (versions: $($versions.Count))"
    }
}

```
### Clean by leaving last 4 versions
```sh
$functions = aws lambda list-functions --query 'Functions[*].FunctionName' --output text

foreach ($fn in $functions.Split("`t")) {
    Write-Host "=== Checking versions for $fn ==="

    # Get versions sorted by LastModified (exclude $LATEST)
    $versions = aws lambda list-versions-by-function --function-name $fn `
        --query 'Versions[?Version!=`$LATEST`].[Version,LastModified]' `
        --output json | ConvertFrom-Json | Sort-Object { $_[1] } -Descending

    if ($versions.Count -gt 4) {
        # Identify versions to delete but do not delete them
        $toDelete = $versions | Select-Object -Skip 4

        foreach ($ver in $toDelete) {
            $verNum = $ver[0]
            Write-Host "Deleting version $verNum of $fn"
            aws lambda delete-function --function-name $fn --qualifier $verNum
        }
    } else {
        Write-Host "No cleanup needed for $fn (versions: $($versions.Count))"
    }
}
```
- Permanent steps identified the missing prune services and implemented. 
### Just print the function name and its version count (>4).
```sh
$functions = aws lambda list-functions --query 'Functions[*].FunctionName' --output text

foreach ($fn in $functions.Split("`t")) {
    $versions = aws lambda list-versions-by-function --function-name $fn --query 'Versions[*]' --output json | ConvertFrom-Json
    $versionCount = $versions.Count

    if ($versionCount -gt 4) {
        Write-Host "=== $fn has $versionCount versions ==="
    }
}
```
Start-Sleep -Seconds 15
$r = Invoke-RestMethod -Uri 'https://api.firecrawl.dev/v2/crawl/019ec686-894d-76e8-b11c-6a3cc5fe9b3d' -Method GET
Write-Host "Status: $($r.status)"
Write-Host "Total: $($r.total)"
Write-Host "Completed: $($r.completed)"
$r | ConvertTo-Json -Depth 20 | Out-File 'C:\Users\ICT-12\Documents\CTF\w3b3\crawl_result.json' -Encoding utf8
Write-Host "Saved."

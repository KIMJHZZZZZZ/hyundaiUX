param([Parameter(Mandatory=$true)][string]$InputDocx,[Parameter(Mandatory=$true)][string]$OutputPdf)
$ErrorActionPreference = 'Stop'
$wordExport = $null
$openedProposal = $null
try {
  $wordExport = New-Object -ComObject Word.Application
  $wordExport.Visible = $false
  $wordExport.DisplayAlerts = 0
  $openedProposal = $wordExport.Documents.Open($InputDocx, $false, $true, $false)
  $openedProposal.Repaginate()
  $pageTotal = $openedProposal.ComputeStatistics(2)
  $openedProposal.ExportAsFixedFormat($OutputPdf, 17)
  Write-Output ('Exported pages: ' + $pageTotal)
  Write-Output $OutputPdf
} finally {
  if ($null -ne $openedProposal) { $openedProposal.Close(0) }
  if ($null -ne $wordExport) { $wordExport.Quit() }
}

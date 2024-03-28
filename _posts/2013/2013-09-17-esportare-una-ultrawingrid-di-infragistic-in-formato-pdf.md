---
title: Esportare una UltraWinGrid di Infragistic in formato Pdf
date: 2013-09-17 14:58:00
tags: c# infragistics pdf
---

Mi sono dovuto picchiare fortissimo con le
[Infragistics](https://www.infragistics.com/ "Infragisitcs") per riuscire
a esportare una UltraWinGrid in un Pdf.

Alla fine ho messo insieme una roba che assomiglia a una classe, con una
funzione che prende come argomenti la griglia, il titolo da dare al pdf
e una lista di stringhe per le colonne che non si vogliono far
visualizzare nel pdf.

Ho aggiunto un pò di commenti per facilitare la vita a chi vorrà farne
uso, sempre se non viene sommerso dalla vastissima documentazione delle
Infragistics. (Si, vabbè, come no...)

```csharp
using System;
using System.Collections.Generic;
using System.Windows.Forms;
using Infragistics.Documents.Reports.Report;
using Infragistics.Documents.Reports.Report.Section;
using Infragistics.Win.UltraWinGrid;

namespace Utils
{
    public class ExportGridPdf
    {
        public void exportGrid(UltraGrid ug, string pdfGridTitle, List<string> hiddenColumns)
        {
            try
            {
                //chiedo dove salvare il pdf
                SaveFileDialog sfd = new SaveFileDialog();
                Infragistics.Win.UltraWinGrid.DocumentExport.UltraGridDocumentExporter ugde = new Infragistics.Win.UltraWinGrid.DocumentExport.UltraGridDocumentExporter();
                sfd.DefaultExt = "pdf";
                sfd.Filter = "PDF files (*.pdf)|*.pdf";
                DialogResult result = sfd.ShowDialog();

                if (result == DialogResult.Cancel)
                    return;

                string fileName = sfd.FileName;

                ugde.AutoSize = Infragistics.Win.UltraWinGrid.DocumentExport.AutoSize.SizeColumnsToContent;

                //qui è l'unico punto in cui specificare se si vuole Landscape o Portrait
                ugde.TargetPaperOrientation = PageOrientation.Landscape;  

                //creo un nuovo report
                Report r = new Report();

                //creo una nuova sezione
                ISection sec = r.AddSection();

                //creo un header che sarà incluso nella sezione
                Infragistics.Documents.Reports.Report.Section.ISectionHeader sectionHeader = sec.AddHeader();
                sectionHeader.Repeat = true;
                sectionHeader.Height = 100;

                //aggiungo un logo
                Infragistics.Documents.Reports.Graphics.Image img = new Infragistics.Documents.Reports.Graphics.Image(Properties.Resources.Logo);
                Infragistics.Documents.Reports.Report.IImage sectionHeaderImg = sectionHeader.AddImage(img, 0, 0);
                sectionHeaderImg.Paddings.All = 10;


                //inserisco il titolo al centro del pdf
                Infragistics.Documents.Reports.Report.Text.IText sectionHeaderText = sectionHeader.AddText(0, 0);
                sectionHeaderText.Paddings.Top = 60;
                sectionHeaderText.Alignment = new TextAlignment(Alignment.Center);
                sectionHeaderText.AddContent(pdfGridTitle);

                //inserisco la data di oggi a sinistra
                Infragistics.Documents.Reports.Report.Text.IText sectionHeaderDate = sectionHeader.AddText(0, 0);
                sectionHeaderDate.Paddings.Top = 60;
                sectionHeaderDate.Alignment = new TextAlignment(Alignment.Left);
                sectionHeaderDate.AddContent(DateTime.Now.ToString("d"));


                //si aggiunge un footer alla section
                Infragistics.Documents.Reports.Report.Section.ISectionFooter sectionFooter = sec.AddFooter();
                sectionFooter.Repeat = true;
                sectionFooter.Height = 60;

                //aggiungo il numeratore di pagina
                Infragistics.Documents.Reports.Report.Text.IText sectionFooterText = sectionFooter.AddText(0, 0);
                sectionFooterText.Alignment = new TextAlignment(Alignment.Left);
                sectionFooterText.AddContent("Page: ");
                sectionFooterText.AddPageNumber(PageNumberFormat.Decimal);

                //nascondo le colonne della grid che non voglio nel pdf
                foreach (string element in hiddenColumns)
                {
                    ug.DisplayLayout.Bands[0].Columns[element].Hidden = true;
                }

                ugde.Export(ug, sec);

                //apro il pdf appena creato
                r.Publish(fileName, FileFormat.PDF);

                //ripristino le colonne che ho nascosto
                foreach (string element in hiddenColumns)
                {
                    ug.DisplayLayout.Bands[0].Columns[element].Hidden = false;
                }
            }
            catch (Exception Ex)
            {
                MessageBox.Show("export pdf fallito: " + Ex.ToString());
            }
        }
    }
}
```

Una nota: cercando di creare il pdf come Landscape, avevo impostato a
Landscape anche la PageOrientation della sezione.  
Contattando il supporto è venuto fuori che le due cose si azzerano a
vicenda, avendo poi come risultato che ci si trova il pdf Portrait.  
Quindi è meglio impostare solo a PageOrientation.Landscape la
TargetPaperOrientation della griglia (riga 31).

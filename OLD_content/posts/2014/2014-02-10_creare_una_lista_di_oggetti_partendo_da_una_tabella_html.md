Title: Creare una lista di oggetti partendo da una tabella html
Date: 2014-02-10 10:12:00
Modified: 2015-03-24 16:09:16
Tags: c#, html, htmlagilitypack, linq, xpath
Slug: creare-una-lista-di-oggetti-partendo-da-una-tabella-html
Author: Doc
Status: Published

Al momento sto lavorando con i Coded UI (un giorno spiegherò cosa sono
e a cosa servono) e ho avuto la necessità di parsare il contenuto di una
tabella html.  
(Abbrevierò il codice con dei [...], tanto sarebbero solo delle
ripetizioni)

Nella tabella ci sono dei dati filtrati e quello che dovevo fare era
verificare il funzionamento del filtro.

La tabella html era così:  

    :::html
    <table id="industrySegmentGrid">
      <tr>
        <td aria-describedby="industrySegmentGrid_Name">aaa</td>
        <td aria-describedby="industrySegmentGrid_Description">bbb</td>
        <td aria-describedby="industrySegmentGrid_IndustrySector">ccc</td>
        <td aria-describedby="industrySegmentGrid_Industry">ddd</td>
        <td aria-describedby="industrySegmentGrid_Status">eee</td>
        <td aria-describedby="industrySegmentGrid_Version">fff/td>
      </tr>
      <tr>
        [...]
      </tr>
    </table>

Ho creato una classe **IndustrySegment** fatta così

    :::c#
    public class IndustrySegment
    {
        private string _name;
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        private string _description;
        public string Description
        {
            get { return _description; }
            set { _description = value; }
        }

        [...]

        public IndustrySegment(string Name, string Description, string Notes, string Sector, string Industry, string Status, string Version)
        {
            _name = Name;
            _description = Description;
            _notes = Notes;
            _sector = Sector;
            _indusrty = Industry;
            _status = Status;
            _version = Version;
        }
    }


A questo punto il mio scopo era creare una lista di oggetti
IndustrySegment contenente tanti oggetti quante righe della tabella e,
dopo lunghe e articolate bestemmie, sono giunto a questa funzione,
sfruttando la comodissima libreria
[HtmlAgilityPack](https://htmlagilitypack.codeplex.com/)

    :::c#
    public List GetIndustrySegments(string HtmlDellaPagina)
    {
        HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
        doc.LoadHtml(HtmlDellaPagina);

        List Results = new List();

        var trList = doc.DocumentNode.SelectSingleNode("//table[@id='industrySegmentGrid']").Descendants("tr");
        foreach (var tr in trList)
        {
            var td = tr.Descendants("td");
            if (td.Count() > 0)
            {
                Results.Add(
                    new IndustrySegment(
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_Name").InnerText,
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_Description").InnerText,
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_Notes").InnerText,
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_IndustrySector").InnerText,
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_Industry").InnerText,
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_Status").InnerText,
                        td.First(x => x.Attributes["aria-describedby"].Value == "industrySegmentGrid_Version").InnerText
                        )
                    );
            }
        }
        return Results;
    }

Non sarà bellissima da leggere, ma funziona :)

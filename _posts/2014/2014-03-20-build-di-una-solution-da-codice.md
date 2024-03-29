---
title: Build di una solution da codice
date: 2014-03-20 16:05:00
tags: c# visual-studio msdn
---

Come seguito al [post precedente]({% post_url 2014/2014-03-07-get-latest-da-codice-di-un-progetto-su-tfs %}),
ecco una funzioncina per buildare una solution da codice.

Questa funzione NON tiene conto di eventuali build configuration e/o di
progetti unloadati.  
A mio avviso è un bug dell'msbuild (e non l'unico, direi), in quanto,
provando a buildare la stessa solution da codice, da visual studio e da
console si ottengono SEMPRE risultati diversi.

Ho chiesto all'inutile-come-sempre supporto msdn, ma mi solo solo fatto
del gran nervoso, ecco il
[link](https://social.msdn.microsoft.com/Forums/vstudio/en-US/0f2bb4fc-c9dd-4dfc-8791-338ceac04c1c/remove-projects-from-a-solution-programmatically)
alla discussione.

```csharp
public static bool BuildSolution()
{
    bool result = false;
    try
    {
        string solutionPath = @"C:\path\della\solution.sln";

        ProjectCollection pc = new ProjectCollection();

        //definiamo le property della build (ci sono miliardi di opzioni diverse)
        Dictionary<string, string=""> globalProperty = new Dictionary<string, string="">();
        globalProperty.Add("Configuration", "Release");
        globalProperty.Add("Platform", "Any CPU");
        globalProperty.Add("OutputPath", "bin\Debug");

        BuildParameters bp = new BuildParameters(pc);
        BuildRequestData BuidlRequest = new BuildRequestData(solutionPath, globalProperty, "4.0", new string[] { "Build" }, null);
        BuildResult buildResult = BuildManager.DefaultBuildManager.Build(bp, BuidlRequest);

        //questo è il modo più semplice per controllare che la build sia andata a buon fine
        if (buildResult.OverallResult == BuildResultCode.Success)
        {
            Console.WriteLine("Build eseguita correttamente");
            result = true;
        }
        else
            //a volte succede che l'exception sia null
            if (buildResult.Exception == null)
                Console.WriteLine("Build fallita: lista errori non disponibile");
            else
                Console.WriteLine("Build fallita: " + buildResult.Exception.ToString());
    }
    catch (Exception e)
    {
        Console.WriteLine("Build Fallita: " + e.ToString());
    }
    return result;
}
```


Quando si è in cerca di soluzioni relative all'ambiente .NET, consiglio
di evitare come la peste tutto quello che nell'url ha "msdn".  
Rispondono alle discussioni esclusivamente per aumentare il loro post
count nella speranza di ottenere qualche punto per poi bullarsi di
essere "MSMVP", un titolo che mi sembra che venga dato assolutamente a
caso.  
Si segnano come risposte i loro post inutili, aumentandosi il rank da
soli.

"Non mi builda la soluzione"  
"Hai provato a buildare?"  
"Ma ho appena detto che..."  
"Ma se buildi da console?"  
"Ma veramente..."  
"La soluzione ti builda?"  
"..."

---*"La soluzione ti builda?" è stata segnata come risposta al thread*

E ricordate, se avrete a che fare con il supporto msdn sappiate che
sarete nel torto a prescindere.  
Visual Studio non ha bachi, il problema sarà sicuramente sempre colpa
vostra.

![mabaffanculo](/assets/img/posts/2014/orsobaffanculo.png)

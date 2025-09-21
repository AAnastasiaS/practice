library ProjectISAPI;

uses
  Web.WebBroker,
  Web.Win.ISAPIApp,
  WebModuleUnit1 in 'WebModuleUnit1.pas' {WebModule1: TWebModule};

exports
  GetExtensionVersion,
  HttpExtensionProc,
  TerminateExtension;

{$R *.res}

begin
  Application.Initialize;
  Application.WebModuleClass := WebModuleClass;
  Application.Run;
end.
